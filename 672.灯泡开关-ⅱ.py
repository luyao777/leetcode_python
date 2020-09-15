#
# @lc app=leetcode.cn id=672 lang=python3
#
# [672] 灯泡开关 Ⅱ
#

# @lc code=start
class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if n == 0 or m == 0:
            return 1
        elif n == 1:
            return 2
        elif n == 2:
            if m == 1:
                return 3
            else:
                return 4
        elif m == 1:
            return 4
        elif m == 2:
            return 7
        else:
            return 8

# @lc code=end

