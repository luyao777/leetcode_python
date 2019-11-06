'''
@Author: Yao Lu
@Date: 2019-11-06 13:40:10
@Description: 
'''

#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import sys
        min_price = sys.maxsize
        max_price = 0
        cur_profile = 0
        profile = 0
        for num, price in enumerate(prices):
            if (price < min_price):
                min_price = price
            if price - min_price > cur_profile:
                cur_profile = price - min_price
                max_price = price
            if price < max_price or num == len(prices) - 1:
                profile += cur_profile
                max_price = 0
                min_price = price
                cur_profile = 0

        return profile


# @lc code=end
