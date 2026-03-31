class Solution:
    def to2D(self, i: int, num_cols: int) -> List[int]:
        x = i // num_cols
        y = i % num_cols
        return x, y

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        l, r = 0, num_rows * num_cols - 1

        while l <= r:
            m = l + ((r - l) // 2)
            x, y = self.to2D(m, num_cols)
            if target < matrix[x][y]:
                r = m - 1
            elif target > matrix[x][y]:
                l = m + 1
            else:
                return True
        
        return False