#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_len = len(nums) + 1
        sum_nums = sum(nums)
        true_sum = int(nums_len * (nums_len-1) / 2)
        return true_sum - sum_nums

# @lc code=end

