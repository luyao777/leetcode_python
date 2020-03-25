#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        judge = True
        if n < 0:
            n = -n
            judge = False
        final = 1
        while n > 0:
            if n & 1:  #代表是奇数
                final *= x
            x *= x
            n >>= 1  # 右移一位
        return final if judge else 1 / final


# @lc code=end
