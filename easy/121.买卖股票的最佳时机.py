'''
@Author: Yao Lu
@Date: 2019-11-05 19:56:28
@Description: 
'''
#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import sys
        min_price = sys.maxsize
        max_price = 0
        profile = 0
        for price in prices:
            if (price < min_price):
                min_price = price
            elif (price - min_price > profile):
                profile = price - min_price
        return profile
        
# @lc code=end

