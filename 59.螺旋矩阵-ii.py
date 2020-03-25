#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        state = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        state[i][j] = 1
        count = n**2 - 1
        while (count):
            while (j < n - 1 and state[i][j + 1] == 0):
                j += 1
                state[i][j] = n**2 - count + 1
                count -= 1
            while (i < n - 1 and state[i + 1][j] == 0):
                i += 1
                state[i][j] = n**2 - count + 1
                count -= 1
            while (j > 0 and state[i][j - 1] == 0):
                j -= 1
                state[i][j] = n**2 - count + 1
                count -= 1
            while (i > 0 and state[i - 1][j] == 0):
                i -= 1
                state[i][j] = n**2 - count + 1
                count -= 1
        return state


# @lc code=end
