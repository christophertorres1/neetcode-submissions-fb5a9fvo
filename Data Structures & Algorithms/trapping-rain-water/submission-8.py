class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        water_step = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                if water_step > height[l]:
                    max_water += water_step - height[l]
                water_step = max(water_step, height[l])
                l += 1
            elif height[r] < height[l]:
                if water_step > height[r]:
                    max_water += water_step - height[r]
                water_step = max(water_step, height[r])
                r -= 1
            else:
                if water_step > height[l]:
                    max_water += water_step - height[l]
                    max_water += water_step - height[r]
                water_step = max(water_step, height[l])
                l += 1
                r -= 1
            if l == r and water_step > height[l]:
                max_water += water_step - height[l]
        
        return max_water