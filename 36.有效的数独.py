#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import numpy as np
        board = np.array(board)

        row = np.zeros((10, 10))
        column = np.zeros((10, 10))
        group = np.zeros((10, 10))

        for i in range(9):
            for j in range(9):
                if board[i, j] == '.':
                    continue
                num = int(board[i, j])
                if row[i][num] == 0 and column[j][num] == 0 and group[i // 3 * 3 + j // 3][num] == 0:
                    row[i][num] = 1
                    column[j][num] = 1
                    group[i // 3 * 3 + j // 3][num] = 1
                else:
                    return False

        return True


# @lc code=end
