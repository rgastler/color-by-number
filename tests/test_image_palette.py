from pathlib import Path
from color_by_number.image_processing import extract_unique_colors
from color_by_number.palette import assign_letters_to_colors


def test_palette_from_image():
    test_image = Path(__file__).parent / "test_image.png"
    colors = extract_unique_colors(str(test_image))
    mapping = assign_letters_to_colors(colors)

    print("Detected colors:")
    for color, letter in mapping.items():
        print(letter, color)

    assert len(colors) == 5


if __name__ == "__main__":
    test_palette_from_image()