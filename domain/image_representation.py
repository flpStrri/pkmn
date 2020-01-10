import numpy as np


class ImageRepresentation:
    def __init__(self, path: str, image_pixels: np.ndarray):
        non_empty_pixels = [rgba_pixel[:-1] for rgba_pixel in image_pixels if rgba_pixel[3] != 0]

        self.path: str = path
        self.raw_image_pixels: np.ndarray = image_pixels
        self.non_empty_pixels: np.ndarray = np.array(non_empty_pixels)
        self.non_empty_pixel_count: int = len(image_pixels) - len(non_empty_pixels)
        # Alexa play Whats wave > Playing Shape of You
