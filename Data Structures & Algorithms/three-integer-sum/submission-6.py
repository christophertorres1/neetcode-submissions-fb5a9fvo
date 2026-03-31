class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            else:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    total = n + nums[j] + nums[k]
                    if total > 0:
                        k -= 1
                    elif total < 0:
                        j += 1
                    else:
                        output.append([n, nums[j], nums[k]])
                        j += 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
        return output
