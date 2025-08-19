from arrays.bubble_sort import bubble_sort
import pytest

testdata = [
    ([3, 2, 1, 0]),
    ([12, 123, -2, 1, 10, 90, 23, 24, 534]),
    ([0.4, 0.3, 0.2, 0.1])
]

@pytest.mark.parametrize("nums", testdata)
def test_bubble_sort(nums: list[int]):

    sorted_nums = bubble_sort(nums)

    nums.sort()

    for i, num in enumerate(nums):
        assert sorted_nums[i] == num

