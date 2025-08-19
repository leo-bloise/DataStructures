def binary_search(nums: list[int], needle: int) -> bool:
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = int((l + r) / 2)

        if nums[m] == needle:
            return True

        if nums[m] > needle:
            r = m - 1
        else:
            l = m + 1
    
    return False

if __name__ == '__main__':
    binary_search([1, 2, 3, 4, 5], 2)