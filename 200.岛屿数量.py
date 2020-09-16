#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        m = len(grid)
        n = len(grid[0])
        island_num = 0
        visited = [[0 for _ in range(n)] for _ in range(m)]

        def visit(grid, i, j):
            if visited[i][j] or grid[i][j] == '0':
                return
            visited[i][j] = 1
            if i > 0:
                visit(grid, i-1, j)
            if j > 0:
                visit(grid, i, j-1)
            if i < m-1:
                visit(grid, i+1, j)
            if j < n-1:
                visit(grid, i, j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    island_num += 1
                    visit(grid, i, j)
        
        return island_num



# @lc code=end

