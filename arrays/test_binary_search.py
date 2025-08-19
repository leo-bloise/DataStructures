from arrays.binary_search import binary_search
import pytest

testdata = [
    ([0, 1, 2, 3, 4, 5], 5, True),
    ([0, 1, 2, 3, 4, 5], 0, True),
    ([0, 1, 2, 3, 4, 5], 4, True),
    ([0, 1, 2, 3, 4, 5], 10, False),
]

@pytest.mark.parametrize("nums,needle,expected", testdata)
def test_binary_search(nums, needle, expected):
    assert binary_search(nums, needle) == expected