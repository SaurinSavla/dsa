from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in range(len(tokens)):
            ch = tokens[i]
            if (ch == '+' or ch == '-' or ch == '*' or ch == '/'):
                num1 = stack.pop()
                num2 = stack.pop()
                if ch == '+':
                    res = int(num2) + int(num1)
                if ch == '-':
                    res = int(num2) - int(num1)
                if ch == '*':
                    res = int(num2) * int(num1)
                if ch == '/':
                    res = int(num2) / int(num1)
                stack.append(res)
            else:
                stack.append(ch)

        return int(stack[-1])