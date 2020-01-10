import numpy as np

from service.pkmn_image_manager import PkmnImageManager


def test_image_to_pixels():
    pkmn_image_manager = PkmnImageManager()
    pixel_array = pkmn_image_manager._get_image_pixel_array(image_path="data/images/1.png")
    assert isinstance(pixel_array, np.ndarray)
    assert pixel_array.shape[1] == 4

    other_pixel_array = pkmn_image_manager._get_image_pixel_array(image_path="data/images/2.png")
    assert not np.array_equal(pixel_array, other_pixel_array)
