from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0] * n
        suffix_max = [0] * n
        prefix_max[0] = height[0]
        suffix_max[n-1] = height[n-1]
        trap_water = 0
        for i in range(1, len(height)):
            prefix_max[i] = max(height[i], prefix_max[i-1])
        for i in range (len(height)-2, -1, -1):
            suffix_max[i] = max(height[i], suffix_max[i+1])
        for i in range(len(height)):
            water = min(prefix_max[i], suffix_max[i]) - height[i]
            trap_water += water
        return trap_water