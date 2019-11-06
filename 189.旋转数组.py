'''
@Author: Yao Lu
@Date: 2019-11-06 19:26:58
@Description: 
'''
#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            item = nums.pop()
            nums.insert(0, item)
        
# @lc code=end

