from torch import FloatTensor, bmm
from torch.nn import Module, Parameter, Sequential, Upsample, ReflectionPad2d, Conv2d, InstanceNorm2d, ReLU


class CoMatchLayer(Module):
    def __init__(self, channels, batch_size=1):
        super().__init__()

        self.C = channels
        self.weight = Parameter(FloatTensor(1, channels, channels), requires_grad=True)
        self.GM_t = FloatTensor(batch_size, channels, channels).requires_grad_()

        # Weight Initialization
        self.weight.data.uniform_(0.0, 0.02)

    def set_targets(self, GM_t):
        self.GM_t = GM_t

    def forward(self, x):
        self.P = bmm(self.weight.expand_as(self.GM_t), self.GM_t)
        return bmm(self.P.transpose(1, 2).expand(x.size(0), self.C, self.C), x.view(x.size(0), x.size(1), -1)).view_as(x)


class ConvBlock(Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride, upsample=False):
        super().__init__()

        self.upsample = Upsample(scale_factor=2) if upsample else None
        self.padding = ReflectionPad2d(kernel_size // 2) if kernel_size // 2 else None
        self.conv = Conv2d(in_channels, out_channels, kernel_size, stride)

    def forward(self, x):
        if self.upsample:
            x = self.upsample(x)
        if self.padding:
            x = self.padding(x)
        return self.conv(x)


class ResBlock(Module):

    expansion = 4

    def __init__(self, in_channels, channels, stride=1, downsample=False, upsample=False):
        super().__init__()

        self.down_conv = Conv2d(in_channels, channels * self.expansion, kernel_size=1, stride=stride) if downsample else None
        self.up_conv = ConvBlock(in_channels, channels * self.expansion, kernel_size=1, stride=1, upsample=upsample) if upsample else None

        self.conv_block = Sequential(InstanceNorm2d(in_channels), ReLU(),
                                     Conv2d(in_channels, channels, kernel_size=1, stride=1),
                                     InstanceNorm2d(channels), ReLU(),
                                     ConvBlock(channels, channels, kernel_size=3, stride=stride, upsample=upsample),
                                     InstanceNorm2d(channels), ReLU(),
                                     Conv2d(channels, channels * self.expansion, kernel_size=1, stride=1))

    def forward(self, x):
        residual = x
        if self.down_conv:
            residual = self.down_conv(x)
        if self.up_conv:
            residual = self.up_conv(x)
        return self.conv_block(x) + residual


class MSGNet(Module):
    def __init__(self, in_channels=3, out_channels=3, channels=128, num_res_blocks=6):
        super().__init__()

        # Siamese Network
        self.siamese_network = Sequential(ConvBlock(in_channels, 64, kernel_size=7, stride=1),
                                          InstanceNorm2d(64), ReLU(),
                                          ResBlock(64, 32, stride=2, downsample=True),
                                          ResBlock(32 * ResBlock.expansion, channels, stride=2, downsample=True))

        # CoMatch Layer
        self.comatch_layer = CoMatchLayer(channels * ResBlock.expansion)

        # Transformation Network
        self.transformation_network = Sequential(self.siamese_network,
                                                 self.comatch_layer,
                                                 *[ResBlock(channels * ResBlock.expansion, channels) for _ in range(num_res_blocks)],
                                                 ResBlock(channels * ResBlock.expansion, 32, stride=1, upsample=True),
                                                 ResBlock(32 * ResBlock.expansion, 16, stride=1, upsample=True),
                                                 InstanceNorm2d(16 * ResBlock.expansion), ReLU(),
                                                 ConvBlock(16 * ResBlock.expansion, out_channels, kernel_size=7, stride=1))

    def gram_matrix(self, inputs):
        BS, C, H, W = inputs.size()
        inputs = inputs.view(BS, C, H * W)
        GM = inputs.bmm(inputs.transpose(1, 2))
        return GM.div_(C * H * W)

    def set_targets(self, x):
        targets = self.siamese_network(x)
        GM_t = self.gram_matrix(targets)
        self.comatch_layer.set_targets(GM_t)

    def forward(self, x):
        return self.transformation_network(x)
