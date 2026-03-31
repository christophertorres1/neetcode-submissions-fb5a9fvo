class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        
        l = 0
        r = 0
        sub_count = {}
        while r < len(s2):
            if r < len(s1) - 1:
                sub_count[s2[r]] = sub_count.get(s2[r], 0) + 1
                r += 1
            else:
                sub_count[s2[r]] = sub_count.get(s2[r], 0) + 1
                if sub_count == s1_count:
                    return True
                sub_count[s2[l]] -= 1
                if sub_count[s2[l]] == 0:
                    del sub_count[s2[l]]
                l += 1
                r += 1
        return False
