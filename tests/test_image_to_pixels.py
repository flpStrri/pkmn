import numpy as np

from services.pkmn_image_manager import PkmnImageManager


def test_image_to_pixels():
    pkmn_image_manager = PkmnImageManager()
    pixel_array = pkmn_image_manager.get_pkmn_image_pixel_array(pkmn_nb=16)
    assert isinstance(pixel_array, np.array)
    assert isinstance(pixel_array.shape[1], 3)
