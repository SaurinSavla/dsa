from typing import List
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        count = 0
        for i in range (1, len(target)):
            count += max(0, target[i] - target[i-1])
        return count + target[0]