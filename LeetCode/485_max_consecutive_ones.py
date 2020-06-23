from typing import List
import time

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    consecs = 0
    max_consecs = 0

    # if nums.count(1) == 0:
    #     return consecs
    # elif nums.count(0) == 0:
    #     return consecs + len(nums)

    for i in range(len(nums)):
        if nums[i] == 1:
            consecs += 1
        else:
            consecs = 0

        if max_consecs < consecs:
            max_consecs = consecs

    return max_consecs

start = time.time()
print(findMaxConsecutiveOnes([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
print("Runtime:", time.time() - start)