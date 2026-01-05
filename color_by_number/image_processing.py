from PIL import Image
from typing import List, Tuple, cast

Color = Tuple[int, int, int]
PixelGrid = List[List[Color]]


def image_to_pixel_grid(
        image: Image.Image,
        grid_width: int,
        grid_height: int,
) -> PixelGrid:
    if grid_width <= 0 or grid_height <= 0:
        raise ValueError("Grid dimensions must be positive.")

    img_width, img_height = image.size

    if grid_width > img_width or grid_height > img_height:
        raise ValueError("Grid dimensions cannot exceed image dimensions.")

    cell_width = img_width / grid_width
    cell_height = img_height / grid_height

    grid: PixelGrid = []

    for row in range(grid_height):
        row_colors: List[Color] = []

        for col in range(grid_width):
            center_x = int((col + 0.5) * cell_width)
            center_y = int((row + 0.5) * cell_height)

            # Clamp just in case floating-point math hits an edge
            center_x = min(center_x, img_width - 1)
            center_y = min(center_y, img_height - 1)

            color = image.getpixel((center_x, center_y))
            row_colors.append(color)

        grid.append(row_colors)

    return grid


def extract_unique_colors(image_path: str) -> List[Tuple[int, int, int]]:
    """
    Load an image and return a list of unique RGB colors.
    """
    img = Image.open(image_path).convert("RGB")
    pixels = list(img.get_flattened_data())

    unique_colors = cast(List[Tuple[int, int, int]], list(set(pixels)))
    return unique_colors

