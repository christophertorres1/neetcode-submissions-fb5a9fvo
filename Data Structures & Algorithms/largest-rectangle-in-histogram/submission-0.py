class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        stack = []
        for i in range(len(heights)):
            boundary = i
            while stack and heights[i] < stack[-1][1]:
                popped_tuple = stack.pop()
                area = (i - popped_tuple[0]) * popped_tuple[1]
                max_area = max(area, max_area)
                boundary = popped_tuple[0]
            stack.append((boundary, heights[i]))
        
        while stack:
            popped_tuple = stack.pop()
            area = (len(heights) - popped_tuple[0]) * popped_tuple[1]
            max_area = max(area, max_area)

        return max_area

