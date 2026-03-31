class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < len(s) and right >= 0:
            if left < right:
                if not s[left].isalnum():
                    left += 1
                elif not s[right].isalnum():
                    right -= 1
                else:
                    if s[left].lower() == s[right].lower():
                        left += 1
                        right -= 1
                    else:
                        return False
            else:
                return True
