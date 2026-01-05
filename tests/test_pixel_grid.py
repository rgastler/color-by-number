import pytest
from PIL import Image
from pathlib import Path

from color_by_number.image_processing import image_to_pixel_grid


@pytest.fixture
def test_image() -> Image.Image:
    """
    Load the small 10x10 test image for pixel grid tests.
    """
    image_path = Path(__file__).parent / "test_image.png"
    return Image.open(image_path).convert("RGB")


def test_grid_shape(test_image):
    grid = image_to_pixel_grid(test_image, grid_width=5, grid_height=5)

    assert len(grid) == 5
    assert  all(len(row) == 5 for row in grid)


def test_grid_too_large_raises(test_image):
    with pytest.raises(ValueError):
        image_to_pixel_grid(test_image, grid_width=20, grid_height=20)


def test_center_pixel_color(test_image):
    grid = image_to_pixel_grid(test_image, grid_width=5, grid_height=5)

    # Adjust this to match your actual test image
    assert grid[0][0] == (237, 28, 36)