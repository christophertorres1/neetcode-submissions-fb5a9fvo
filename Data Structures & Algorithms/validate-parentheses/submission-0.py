class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            else:
                if stack and char == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True