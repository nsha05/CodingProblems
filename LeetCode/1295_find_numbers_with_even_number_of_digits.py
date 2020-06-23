from typing import List

def findNumbers(nums: List[int]) -> int:
    evens = 0

    for i in range(len(nums)):
        digits = 0
        while nums[i] > 0:
            nums[i] = int(nums[i]/10)
            digits += 1

        if digits % 2 == 0:
            evens += 1

    return evens

print(findNumbers([12,345,2,6,7896]))