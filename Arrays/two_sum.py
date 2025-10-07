from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(0, len(nums)):
            j = target - nums[i]
            if j in hashmap:
                return [i, hashmap[j]]
            hashmap[nums[i]] = i
        return []  