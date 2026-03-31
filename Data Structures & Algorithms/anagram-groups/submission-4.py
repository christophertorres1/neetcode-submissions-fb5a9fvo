class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for str in strs:
            signature = "".join(sorted(str))
            if signature in hash_map:
                hash_map[signature].append(str)
            else:
                hash_map[signature] = [str]
        
        output_arr = []
        for subarr in hash_map.values():
            output_arr.append(subarr)
        return output_arr