#
# @lc app=leetcode.cn id=1561 lang=python3
#
# [1561] 你可以获得的最大硬币数目
#

# @lc code=start
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        res = 0
        while(piles):
            piles.pop(0)
            res += piles.pop(0)
            piles.pop(-1)
        return res
        # print(piles)
# @lc code=end

