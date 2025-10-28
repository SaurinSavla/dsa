from typing import List
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        prefix[0] = 0
        for i in range (1, len(nums)):
            prefix[i] = prefix [i-1] + nums[i-1]
        suffix = [0] * len(nums)
        suffix[len(nums)-1] = 0
        for i in range (len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] + nums[i+1]
        print(prefix)
        print(suffix)
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                if prefix[i] == suffix[i]:
                    count += 2
                if prefix[i]-1 == suffix[i]:
                    count += 1
                if prefix[i] == suffix[i]-1:
                    count += 1
        return count