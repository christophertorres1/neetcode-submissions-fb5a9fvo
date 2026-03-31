class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        delim = "#"
        for s in strs:
            s_len = len(s)
            encoded_string += str(s_len) + delim + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        while s:
            i_delim = s.find("#")
            s_len = int(s[:i_delim])
            i_start = i_delim + 1
            i_end = i_delim + s_len + 1
            strs.append(s[i_start : i_end])
            s = s[i_end:]
        return strs
