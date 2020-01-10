import numpy as np

from service.colors_manager import ColorsManager


def test_calculate_colors_complexity():
    colors_manager = ColorsManager()
    colors_array = np.ones((10, 3))
    colors_complexity = colors_manager.calculate_colors_complexity(colors_array)
    assert colors_complexity == 0

    colors_array[0, 0] = 2
    colors_complexity = colors_manager.calculate_colors_complexity(colors_array)
    assert colors_complexity > 0
