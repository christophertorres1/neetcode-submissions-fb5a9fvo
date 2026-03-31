class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in prevMap:
                return [prevMap[remainder], i]
            prevMap[num] = i
        