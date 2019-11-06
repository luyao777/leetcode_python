'''
@Author: Yao Lu
@Date: 2019-11-06 19:41:59
@Description: 
'''
#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur


        
# @lc code=end

