import numpy as np

from service.main_colors_calculator import MainColorsCalculator


def test_calculate_main_colors():
    main_colors_calculator = MainColorsCalculator()
    strange_pixel_list = np.random.randint(0, 256, (96 * 96, 3))
    colors = main_colors_calculator.calculate_main_colors(strange_pixel_list, n_colors=10)
    assert colors.shape == (10, 3)
    for color in colors:
        for rgb_value in color:
            assert int(rgb_value) == rgb_value
