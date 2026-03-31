class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        total = 1
        for num in nums:
            total *= num
            prefix.append(total)
        
        suffix = []
        total = 1
        for num in reversed(nums):
            total *= num
            suffix.append(total)
        suffix = list(reversed(suffix))

        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(suffix[i+1])
            elif i == len(nums) - 1:
                output.append(prefix[i-1])
            else:
                output.append(prefix[i-1] * suffix[i+1])
        return output