#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]

        # n = len(nums)
        # def new_rob(nums, first_flag=False):
        #     if len(nums) == 0:
        #         return 0
        #     elif len(nums) == 1:
        #         if first_flag:
        #             return 0
        #         else:
        #             return nums[0]
        #     elif len(nums) == 2:
        #         if first_flag:
        #             return nums[0]
        #         else:
        #             return max(nums)
            
        #     if first_flag:
        #         return max(new_rob(nums[1:], first_flag), nums[0] + new_rob(nums[2:], first_flag))
        #     elif len(nums) == n:
        #         return max(new_rob(nums[1:]), nums[0] + new_rob(nums[2:], True))
        #     else:
        #         return max(new_rob(nums[1:]), nums[0] + new_rob(nums[2:]))
        # return new_rob(nums)
# @lc code=end

