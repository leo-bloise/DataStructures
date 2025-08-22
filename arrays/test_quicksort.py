from arrays.quicksort import quicksort
import pytest

testdata = [
    ([3, 2, 1, 0]),
    ([12, 123, -2, 1, 10, 90, 23, 24, 534]),
    ([0.4, 0.3, 0.2, 0.1])
]

@pytest.mark.parametrize("nums", testdata)
def test_quicksort(nums: list[int]):
    sorted = quicksort(nums)

    nums.sort()

    for index, num in enumerate(nums):
        assert sorted[index] == num
