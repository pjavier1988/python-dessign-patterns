import pytest

from decorator import Circle


@pytest.fixture(scope="module")
def circle():

    circle = Circle(2)
    return circle


def test_area(circle):
    assert circle.area == 12.5664


def test_negative_numbers_on_set_radius_raise_value_error(circle):
    with pytest.raises(ValueError):
        circle.radius = -4