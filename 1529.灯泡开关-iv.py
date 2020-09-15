#
# @lc app=leetcode.cn id=1529 lang=python3
#
# [1529] 灯泡开关 IV
#

# @lc code=start
class Solution:
    def minFlips(self, target: str) -> int:
        nums_1, nums_0 = 0, 0
        i = len(target) - 1
        while(i >= 0):
            if i >= 0 and target[i] == '1':
                nums_1 += 1
            while(i >= 0 and target[i] == '1'):
                i -= 1
            if i >= 0 and target[i] == '0':
                nums_0 += 1
            while(i >= 0 and target[i] == '0'):
                i -= 1
        if target[0] == '0':
            nums_0 -= 1
        # print(nums_0, nums_1)
        return nums_0 + nums_1

# @lc code=end

