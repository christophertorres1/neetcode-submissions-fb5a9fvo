class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find minimum to disect into two increasing arrays
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        min_i = l

        # check if we are binary searching the full array or one half
        if min_i == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0]:
            l, r = 0, min_i - 1
        else:
            l, r = min_i, len(nums) - 1

        # binary search the target subarray
        while l < r:
            m = l + ((r - l) // 2)
            if target > nums[m]:
                l = m + 1
            else:
                r = m
        
        return l if nums[l] == target else -1