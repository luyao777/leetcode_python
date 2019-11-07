'''
@Author: Yao Lu
@Date: 2019-11-07 16:46:39
@Description: 
'''
#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        return True if len(nums) != len(nums_set) else False
        
# @lc code=end

