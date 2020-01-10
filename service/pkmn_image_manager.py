import numpy as np
from PIL import Image

from domain.image_representation import ImageRepresentation
from service.colors_manager import ColorsManager


class PkmnImageManager:
    @classmethod
    def get_colors_from_path(cls, path: str) -> np.ndarray:
        pixel_array = cls._get_image_pixel_array(path)
        representation = ImageRepresentation(path, pixel_array)
        colors = cls._get_colors_from_pixel_array(representation.non_empty_pixels)
        return colors

    @staticmethod
    def _get_image_pixel_array(image_path: str) -> np.ndarray:
        image = Image.open(image_path).convert("RGBA")
        image_width, image_height = image.size

        image_pixels = list()

        for x in range(1, image_width):
            for y in range(1, image_height):
                pixVal = image.getpixel((x, y))
                image_pixels.append(pixVal)
        
        return np.array(image_pixels)

    @staticmethod
    def _get_colors_from_pixel_array(pixel_array: np.ndarray) -> np.ndarray:
        return ColorsManager.calculate_main_colors(pixel_array)
