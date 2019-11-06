'''
@Author: Yao Lu
@Date: 2019-11-06 16:31:55
@Description: 
'''
#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {}
        for ele in nums:
            if ele not in num_dict.keys():
                num_dict[ele] = 1
            else:
                num_dict[ele] += 1
        result_num = -1
        result_count = 0
        for key in num_dict.keys():
            if num_dict[key] > result_count:
                result_num = key
                result_count = num_dict[key]
        return result_num

        
# @lc code=end

