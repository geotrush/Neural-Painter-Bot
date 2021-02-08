from datetime import datetime
from torch import load, no_grad

from fast_style_transfer.utils import *
from fast_style_transfer.network import *


class FNST:
    '''
    Inference stage for
    Fast Neural Style Transfer with MSG-Net
    '''
    def __init__(self, content_path, style_path):
        # Start the clock
        self.time_started = self._start_clock()

        # Prepare images
        self.content = prep(content_path)
        self.style = prep(style_path)

        # Define network in evaluation mode
        self.model = MSGNet().eval()

        # Load model pretrained on 21 styles
        self.model.load_state_dict(load(f'fast_style_transfer/msgnet_21_styles.pth', map_location='cpu'))

        # Pre-compute style targets
        self.model.set_targets(self.style)

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
