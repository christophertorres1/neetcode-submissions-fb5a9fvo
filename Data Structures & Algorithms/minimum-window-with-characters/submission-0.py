class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest_sub = ""
        shortest_len = float("inf")

        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        need = len(t_count)

        sub_count = {}
        have = 0

        l = r = 0
        while r < len(s):
            if s[r] in t_count:
                sub_count[s[r]] = sub_count.get(s[r], 0) + 1
                if sub_count[s[r]] == t_count[s[r]]:
                    have += 1
                    while have == need:
                        if len(s[l:r+1]) < shortest_len:
                            shortest_sub = s[l:r+1]
                            shortest_len = len(s[l:r+1])
                        if s[l] in sub_count:
                            sub_count[s[l]] -= 1
                            if sub_count[s[l]] < t_count[s[l]]:
                                have -= 1
                        l += 1 
            r += 1
        
        return shortest_sub