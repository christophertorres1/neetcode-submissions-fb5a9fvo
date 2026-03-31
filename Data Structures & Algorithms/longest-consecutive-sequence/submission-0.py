class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        len_longest = 0
        for num in nums:
            if num - 1 not in nums_set:
                len_sequence = 0
                n = num
                while n in nums_set:
                    len_sequence += 1
                    n += 1
                len_longest = max(len_longest, len_sequence)
        
        return len_longest
