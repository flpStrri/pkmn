import numpy as np
from scipy.spatial.distance import cdist

from sklearn.cluster import KMeans


class ColorsManager:
    @classmethod
    def calculate_main_colors(cls, pixels: np.ndarray, n_colors: int = 10) -> np.ndarray:
        _, pixel_dimension = pixels.shape
        if pixel_dimension != 3:
            raise cls.WrongFormat("")
        k_means_model = KMeans(n_colors)
        k_means_model.fit(pixels)
        float_colors_array = k_means_model.cluster_centers_
        return cls._cast_colors_to_int(float_colors_array)

    @staticmethod
    def calculate_colors_complexity(colors: np.ndarray) -> float:
        return float(np.sum(cdist(colors, colors))) / 2

    @staticmethod
    def _cast_colors_to_int(colors_array: np.ndarray) -> np.ndarray:
        return np.rint(colors_array)

    class WrongFormat(Exception):
        pass
