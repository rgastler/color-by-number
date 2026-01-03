import numpy as np
import random
from typing import List, Tuple

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

def assign_letters_to_colors(colors: List[Tuple[int, int, int]]) -> dict:
    """
    Assign a unique letter to each color.

    Args:
        colors: List of RGB tuples, e.g. [(255,0,0), (0,255,0)]

    Returns:
        Dictionary mapping color tuples to letters
    """
    if len(colors) > len(alphabet):
        raise ValueError("Too many colors for available letters")

    letters = alphabet[:len(colors)]
    mapping = {color: letter for color, letter in zip(colors, letters)}

    return mapping

