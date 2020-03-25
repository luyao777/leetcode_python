#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#


# @lc code=start
class Solution:
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    def spiralOrder(self, matrix):
        result = []
        if matrix == []:
            return result
        m, n = len(matrix), len(matrix[0])
        state = [[0 for _ in range(n)] for _ in range(m)]
        i, j = 0, 0
        result.append(matrix[i][j])
        state[i][j] = 1
        count = m * n - 1
        while (count):
            while (j < n - 1 and state[i][j + 1] == 0):
                j += 1
                result.append(matrix[i][j])
                state[i][j] = 1
                count -= 1
            while (i < m - 1 and state[i + 1][j] == 0):
                i += 1
                result.append(matrix[i][j])
                state[i][j] = 1
                count -= 1
            while (j > 0 and state[i][j - 1] == 0):
                j -= 1
                result.append(matrix[i][j])
                state[i][j] = 1
                count -= 1
            while (i > 0 and state[i - 1][j] == 0):
                i -= 1
                result.append(matrix[i][j])
                state[i][j] = 1
                count -= 1
        return result


# @lc code=end
