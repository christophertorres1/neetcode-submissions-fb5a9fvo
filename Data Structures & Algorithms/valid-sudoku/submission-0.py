class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit != ".":
                    if digit in row_sets[i]:
                        return False
                    else:
                        row_sets[i].add(digit)
                        if digit in col_sets[j]:
                            return False
                        else:
                            col_sets[j].add(digit)
                            if digit in box_sets[i//3][j//3]:
                                return False
                            else:
                                box_sets[i//3][j//3].add(digit)
        return True
