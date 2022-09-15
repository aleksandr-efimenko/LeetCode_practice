from typing import List

def findOriginalArray(changed: List[int])-> List[int]:
    if len(changed) % 2 != 0:
        return []
    original = []
    counted_nums = {}
    changed.sort()
    for num in changed:
        counted_nums[num] = counted_nums.get(num, 0) + 1
    print(counted_nums)
    if counted_nums.get(0) is not None:
        if counted_nums.get(0) % 2 == 0:
            original = [0] * int(counted_nums.get(0) / 2)
        else:
            return []

    for key, value in counted_nums.items():
        if counted_nums.get(key * 2, 0) >= counted_nums.get(key) or counted_nums.get(key) == 0:
            if counted_nums.get(key) == 0:
                continue
            counted_nums[key * 2] = counted_nums[key * 2] - counted_nums[key]
            original = original + [key] * counted_nums[key]
            counted_nums[key] = 0
        else:
            return []
    return original

print(findOriginalArray([1,3,3,6,2,4,2,6,8]))