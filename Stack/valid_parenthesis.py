class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ')':
                if not stack or stack[-1] != '(':
                    return False
                elif (stack[-1] == '('):
                    stack.pop()
            elif i == '}':
                if not stack or stack[-1] != '{':
                    return False
                elif (stack[-1] == '{'):
                    stack.pop()
            elif i == ']':
                if not stack or stack[-1] != '[':
                    return False
                elif (stack[-1] == '['):
                    stack.pop()
            else:
                stack.append(i)
        print (stack)
        if stack:
            return False
        else:
            return True
                
                
