#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        raw = []
        col = []

        def set_zero(matrix, i, j):
            if i not in raw:
                raw.append(i)
                for k in range(len(matrix[0])):
                    if matrix[i][k] == 0:
                        set_zero(matrix, i, k)
                    else:
                        matrix[i][k] = 0
            if j not in col:
                col.append(j)
                for k in range(len(matrix)):
                    if matrix[k][j] == 0:
                        set_zero(matrix, k, j)
                    else:
                        matrix[k][j] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i in raw or j in col:
                        continue
                    set_zero(matrix, i, j)
                    


# @lc code=end

