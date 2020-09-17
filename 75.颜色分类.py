#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # for j in range(n):
        #     for i in range(n-j-1):
        #         if nums[i] > nums[i+1]:
        #             nums[i], nums[i+1] = nums[i+1], nums[i]
        # return nums

        # nums_dict = {0: 0, 1: 0, 2: 0}
        # for num in nums:
        #     nums_dict[num] += 1
        # for i in range(len(nums)):
        #     if i < nums_dict[0]:
        #         nums[i] = 0
        #     elif i < nums_dict[0] + nums_dict[1]:
        #         nums[i] = 1
        #     else:
        #         nums[i] = 2

        '''
        荷兰三色旗问题解
        '''
        # 对于所有 idx < p0 : nums[idx < p0] = 0
        # curr是当前考虑元素的下标
        p0 = curr = 0
        # 对于所有 idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1

# @lc code=end
