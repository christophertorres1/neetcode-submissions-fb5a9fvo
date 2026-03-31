class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create frequency hashmap
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        # Bucket sort nums based on their frequency
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, count in counter.items():
            buckets[count].append(num)

        # Choose the k most frequent elements
        k_arr = [num for bucket in reversed(buckets) for num in bucket]
        return k_arr[:k]
