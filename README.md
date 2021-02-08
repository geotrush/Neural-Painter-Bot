# :brain::man_artist::robot: **Neural Painter Bot**

[![forthebadge](https://forthebadge.com/images/badges/made-with-crayons.svg)](https://forthebadge.com)

<img align="center" src="demos/neural_painter_portrait.jpg" width="440" height="512">

## :brain::man_artist: [Neural Painter](https://telegram.me/NeuralPainterBot) is a Telegram Bot that implements neural network solutions to the task of Fast Style Transfer :zap:

## :robot: The Bot supports two modes:

 ### :rainbow: Stylization mode (MSG-Net)
<img src="demos/stylization.gif" width="468" height="472">

 ### :art: Painting mode (CycleGAN)
<img src="demos/painting.gif" width="468" height="472">


## TODO:

- [ ] Add more painting styles

- [ ] Refactor pre-trained CycleGAN model (remove `models/` folder)

- [ ] Refactor style menu code using OOP patterns such as a factory


## :bow: *Acknowledgements*:

- ### *Multi-style Generative Network for Real-time Transfer (Zhang & Dana, 2017)*
    - ### *[arXiv paper](https://arxiv.org/pdf/1703.06953.pdf) & [GitHub repository](https://github.com/zhanghang1989/PyTorch-Multi-Style-Transfer)*

- ### *Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks (Zhu et al., 2017)*
    - ### *[arXiv paper](https://arxiv.org/pdf/1703.10593.pdf) & [GitHub repository](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)*
