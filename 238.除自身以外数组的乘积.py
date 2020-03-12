#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        left, right = 1, 1
        for i in range(len(nums)):
            results.append(left)
            left *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            results[i] = results[i] * right
            right *= nums[i]
        return results


# @lc code=end
