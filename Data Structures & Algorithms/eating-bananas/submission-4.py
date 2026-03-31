class Solution:
    def canFinishOnTime(self, piles: List[int], k: int, h: int) -> bool:
        if k <= 0:
            return False
            
        for pile in piles:
            hrs = math.ceil(pile / k)
            h -= hrs
            if h < 0:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = (r - l) // 2 + l
            if not self.canFinishOnTime(piles, m, h):
                l = m + 1
            elif self.canFinishOnTime(piles, m - 1, h):
                r = m - 1
            else:
                return m