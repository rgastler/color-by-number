from PIL import Image
from typing import List, Tuple, cast


def extract_unique_colors(image_path: str) -> List[Tuple[int, int, int]]:
    """
    Load an image and return a list of unique RGB colors.
    """
    img = Image.open(image_path).convert("RGB")
    pixels = list(img.get_flattened_data())

    unique_colors = cast(List[Tuple[int, int, int]], list(set(pixels)))
    return unique_colors

