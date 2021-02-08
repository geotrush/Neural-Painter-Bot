import numpy as np
from PIL import Image
from torchvision import transforms


# Pre-processing
def prep(image_path, size=350):
    image = Image.open(image_path).convert('RGB')
    image2tensor = transforms.Compose([transforms.Resize(size),
                                       transforms.CenterCrop(size),
                                       transforms.ToTensor()])
    return image2tensor(image).unsqueeze(0)


# Post-processing
def post(tensor):
    tensor.add_(1).div_(2)
    tensor = np.rollaxis(tensor.numpy()[0], 0, 3)
    return Image.fromarray(np.uint8(tensor * 255))
