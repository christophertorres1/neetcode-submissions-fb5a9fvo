class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for str in strs:
            signature = "".join(sorted(str))
            if signature in hash_map:
                hash_map[signature].append(str)
            else:
                hash_map[signature] = [str]

        return list(hash_map.values())