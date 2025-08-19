def swap(nums: list[int], x: int, y: int):
    tmp = nums[y]
    nums[y] = nums[x]
    nums[x] = tmp

def bubble_sort(nums: list[int]) -> list[int]:
    while True:
        swaps = 0
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                swap(nums, i, i + 1)
                swaps += 1
        
        if swaps == 0:
            break
    
    res = []

    for num in nums:
        res.append(num)
    
    return res
