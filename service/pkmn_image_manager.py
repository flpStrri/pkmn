import numpy as np
from PIL import Image
from colr import color as print_color

from domain.image_representation import ImageRepresentation
from service.colors_manager import ColorsManager


class PkmnImageManager:
    @classmethod
    def get_complexity_from_path(cls, path: str, n_colors: int) -> float:
        pixel_array = cls._get_image_pixel_array(path)
        representation = ImageRepresentation(path, pixel_array)
        colors = ColorsManager.calculate_main_colors(representation.non_empty_pixels, n_colors=n_colors)
        for color in colors:
            color_tuple = tuple(color)
            print(print_color('chosen color', fore=color_tuple, back=color_tuple))
        complexity = ColorsManager.calculate_colors_complexity(colors)
        return complexity

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
