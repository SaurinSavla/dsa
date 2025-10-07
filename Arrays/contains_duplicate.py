from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = dict.fromkeys(nums, 0)
        for num in nums:
            unique[num] += 1
        for val in unique.values():
            if val > 1:
                return True
        return False