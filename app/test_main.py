import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat,dog,expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    (24, 28, [2, 2]),])
def test_get_human_age_examples(cat: int, dog: int, expected: list) -> bool:
    assert get_human_age(cat, dog) == expected
