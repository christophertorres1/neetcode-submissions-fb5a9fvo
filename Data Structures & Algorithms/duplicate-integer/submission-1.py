class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_seen = []
        for num in nums:
            if num in nums_seen:
                return True
            nums_seen.append(num)
        return False