from src.utils.parsers import *


# def test_get_absolute_path() -> None:
#     path = "some/path/to/this.something"
#     assert path == get_absolute_path(path)


def test_append_to_image_name() -> None:
    name = "my_very_nice_file_name.extra_cool.jpg"
    res = append_to_image_name(name, "_2")
    assert res == "my_very_nice_file_name.extra_cool_2.jpg"
