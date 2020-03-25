#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#


# @lc code=start
class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    def canJump(self, nums):
        nums_len = len(nums)
        state = [0 for _ in range(nums_len)]
        state[-1] = 1

        if nums_len == 1:
            return True

        i = nums_len - 2
        while (i != -1):
            max_pos = min(i + 1 + nums[i], nums_len)
            if 1 in state[i + 1:max_pos]:
                state[i] = 1
            i -= 1

        if state[0] == 0:
            return False
        else:
            return True

# @lc code=end
