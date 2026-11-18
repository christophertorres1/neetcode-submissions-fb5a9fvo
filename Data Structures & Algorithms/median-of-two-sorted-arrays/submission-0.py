class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)
        idx = len(arr) // 2
        if len(arr) % 2 == 0:
            median = (arr[idx] + arr[idx-1]) / 2
        else:
            median = arr[idx]
        return median