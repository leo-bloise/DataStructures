from arrays.bucket_sorting import bucket_sort
import pytest

testdata = [
    ([3, 2, 1, 0]),
    ([12, 123, -2, 1, 10, 90, 23, 24, 534]),
    ([0.4, 0.3, 0.2, 0.1])
]

@pytest.mark.parametrize("nums", testdata)
def test_bucket_sorting(nums):
    nums = [3, 2, 1, 0]

    sorted = bucket_sort(nums, max(nums), min(nums))

    nums.sort()

    for i, v in enumerate(nums):
        assert v == sorted[i]