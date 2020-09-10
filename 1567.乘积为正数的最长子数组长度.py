#
# @lc app=leetcode.cn id=1567 lang=python3
#
# [1567] 乘积为正数的最长子数组长度
#

# @lc code=start
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pre = -1
        stack = []
        res = 0
        for i, num in enumerate(nums):
            if num < 0:
                stack.append(i)
            elif num == 0:
                stack, pre = [], i
            if len(stack) % 2 == 0:
                res = max(res, i - pre)
            else:
                res = max(res, i - stack[0])
        return res

# @lc code=end
