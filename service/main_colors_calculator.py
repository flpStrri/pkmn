import numpy as np

from sklearn.cluster import KMeans


class MainColorsCalculator:
    def calculate_main_colors(self, pixels: np.ndarray, n_colors: int = 10) -> np.ndarray:
        _, pixel_dimension = pixels.shape
        if pixel_dimension != 3:
            raise self.WrongFormat("")
        k_means_model = KMeans(n_colors)
        k_means_model.fit(pixels)
        float_colors_array = k_means_model.cluster_centers_
        return self._cast_colors_to_int(float_colors_array)

    def _cast_colors_to_int(self, colors_array: np.ndarray) -> np.ndarray:
        return np.rint(colors_array)

    class WrongFormat(Exception):
        pass