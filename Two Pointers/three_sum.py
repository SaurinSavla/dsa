from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range (0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left = i + 1
            right = len(nums)-1
            while left < right:
                if (nums[right] + nums[left] == target):
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif(nums[left] + nums[right] < target):
                    left += 1
                else:
                    right -= 1
        return res