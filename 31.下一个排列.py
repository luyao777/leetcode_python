#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                res_nums = nums[i:]
                res_nums.sort()
                nums[i:] = res_nums
                for j in range(i, len(nums)):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        break
                return
        nums.sort()

# @lc code=end

