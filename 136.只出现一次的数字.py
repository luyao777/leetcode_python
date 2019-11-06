'''
@Author: Yao Lu
@Date: 2019-11-06 14:08:56
@Description: 
'''
#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        double_list = 2*list(nums_set)
        for i in nums:
            double_list.remove(i)
        return double_list[0]
        
# @lc code=end

