from datetime import datetime
from torch import load, no_grad

from painting_mode.utils import *


class GNST:
    '''
    Inference stage for
    Generative Neural Style Transfer with CycleGAN
    '''
    def __init__(self, content_path):
        # Start the clock
        self.time_started = self._start_clock()

        # Prepare images
        self.content = prep(content_path)

        # Load network in evaluation mode
        self.model = load('./generative_style_transfer/cyclegan_van_gogh.pth', map_location='cpu')

    def _start_clock(self):
        return datetime.now()

    def _stop_clock(self):
        # Return inference time in seconds
        time_passed = datetime.now() - self.time_started
        return f'{time_passed.seconds}.{str(time_passed.microseconds)[:2]}'

    def transfer_style(self):
        # Forward pass for inference
        with no_grad():
            output = self.model(self.content)

        # Post-process output image
        output_image = post(output)

        # Stop the clock
        time_passed = self._stop_clock()

        # Return inference result and inference time in seconds
        return output_image, time_passed
