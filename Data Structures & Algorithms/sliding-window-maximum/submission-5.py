import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        max_elements = []
        max_heap = []
        delete_heap = []
        l = r = 0
        while r < len(nums):
            heapq.heappush(max_heap, -nums[r])
            if r - l + 1 < k:
                r += 1
            else:
                max_elements.append(-max_heap[0])
                heapq.heappush(delete_heap, -nums[l])
                l += 1
                r += 1
                while delete_heap and max_heap[0] == delete_heap[0]:
                    heapq.heappop(max_heap)
                    heapq.heappop(delete_heap)
        return max_elements