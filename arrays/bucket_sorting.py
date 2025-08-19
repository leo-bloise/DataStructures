def normalize(val: int, max_val: int, min_val: int) -> int:
    return (val - min_val) / (max_val - min_val + 1)

def bucket_sort(nums: list[int], max_val: int, min_val: int):
    buckets = [None] * len(nums)

    result = []

    for num in nums:
        index_normalized = min(int(normalize(num, max_val, min_val) * len(buckets)), len(buckets) - 1)

        if buckets[index_normalized] is None:
            buckets[index_normalized] = [num]
            continue

        buckets[index_normalized].append(num)
    
    for bucket in buckets:
        if bucket is None:
            continue
        
        bucket.sort()

        for i in bucket:
            result.append(i)
    
    return result