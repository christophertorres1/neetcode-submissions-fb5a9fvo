class Solution:
    def isValid(self, s: str) -> bool:
        pair_map = {'(': ')', '{': '}', '[': ']'}

        stack = []
        for char in s:
            if char in pair_map:
                stack.append(pair_map[char])
            elif stack and stack[-1] == char:
                stack.pop()
            else:
                return False
                
        return not stack