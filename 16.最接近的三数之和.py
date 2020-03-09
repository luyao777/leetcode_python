#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if (not nums or n < 3):
            return None
        nums.sort()
        res = float("inf")
        for i in range(n):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                cur_sum = nums[i] + nums[L] + nums[R]

                if (cur_sum == target):
                    return target
                if (abs(cur_sum - target) < abs(res - target)):
                    res = cur_sum
                if (cur_sum - target < 0):
                    L += 1
                else:
                    R -= 1
        return res


# @lc code=end
