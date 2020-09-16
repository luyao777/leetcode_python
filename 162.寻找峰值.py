#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0, -float('inf'))
        nums.append(-float('inf'))
        for i in range(0, len(nums)):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i-1

# @lc code=end

