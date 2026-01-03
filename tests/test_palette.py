from color_by_number.palette import assign_letters_to_colors


def test_assign_letters_to_colors():
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    mapping = assign_letters_to_colors(colors)

    assert mapping[(255, 0, 0)] in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    assert mapping[(0, 255, 0)] != mapping[(255, 0, 0)]
    assert mapping[(0, 0, 255)] != mapping[(255, 0, 0)]
    print("Test passed!")


if __name__ == "__main__":
    test_assign_letters_to_colors()