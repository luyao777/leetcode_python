'''
@Author: Yao Lu
@Date: 2019-11-06 15:06:34
@Description: 
'''
#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start_p = 0
        end_p = len(numbers)-1
        while(start_p != end_p):
            if numbers[start_p] + numbers[end_p] == target:
                return [start_p+1, end_p+1]
            elif numbers[start_p] + numbers[end_p] > target:
                end_p -= 1
            else:
                start_p += 1        
# @lc code=end

