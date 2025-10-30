from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #pair
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stackt, stackind = stack.pop()
                answer[stackind] = i - stackind
            stack.append([temperatures[i], i])
        return answer