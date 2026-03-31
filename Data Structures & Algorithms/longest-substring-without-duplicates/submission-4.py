class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        max_len = 0
        i = 0
        j = i + 1
        sub_chars = set(s[i])
        sub_len = 1
        while j < len(s):
            if s[j] in sub_chars:
                sub_chars.remove(s[i])
                sub_len -= 1
                i += 1
            else:
                sub_chars.add(s[j])
                sub_len += 1
                max_len = max(sub_len, max_len)
                j += 1
        return max_len
            