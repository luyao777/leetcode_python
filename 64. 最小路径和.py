class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid.copy()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1] + dp[i][j]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + dp[i][j]
        return dp[-1][-1]