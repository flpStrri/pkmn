import numpy as np
from domain.image_representation import ImageRepresentation


class TestCreateImageRepresentation:
    def test_image_representation_creation(self):
        test_path = "/i'm/a/barbie/girl"
        test_image_pixels = np.array([
            (0, 0, 0, 0),
            (0, 0, 2, 255),
            (0, 0, 0, 0),
            (4, 2, 1, 255),
        ])

        test_image_representation = ImageRepresentation(test_path, test_image_pixels)

        assert test_image_representation.path == "/i'm/a/barbie/girl"
        assert np.array_equal(test_image_representation.raw_image_pixels, test_image_pixels)
        assert np.array_equal(test_image_representation.non_empty_pixels, np.array([
            (0, 0, 2),
            (4, 2, 1),
        ]))
        assert test_image_representation.non_empty_pixel_count == 2
