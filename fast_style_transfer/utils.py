from PIL import Image

from torch import LongTensor
import torchvision.transforms as transforms


# Pre-processing
def prep(image_path, size=350):
    image = Image.open(image_path).convert('RGB')
    image = image.resize((size, int(size / image.size[0] * image.size[1])), Image.LANCZOS)
    image2tensor = transforms.Compose([transforms.ToTensor(),
                                       transforms.Lambda(lambda x: x[LongTensor([2, 1, 0])]),
                                       transforms.Lambda(lambda x: x.mul_(255))])
    return image2tensor(image).unsqueeze(0)

# Post-processing
def post(tensor):
    tensor2image = transforms.Compose([transforms.Lambda(lambda x: x.div_(255)),
                                       transforms.Lambda(lambda x: x[LongTensor([2, 1, 0])]),
                                       transforms.ToPILImage()])
    return tensor2image(tensor.squeeze(0).clamp_(0, 255))
