import numpy as np
from PIL import Image


class PkmnImageManager:
    def get_image_pixel_array(self, image_path: str) -> np.ndarray:
        image = Image.open(image_path).convert("RGBA")
        image_width, image_height = image.size

        image_pixels = list()

        for x in range(1, image_width):
            for y in range(1, image_height):
                pixVal = image.getpixel((x, y))
                image_pixels.append(pixVal)
        
        return np.array(image_pixels)