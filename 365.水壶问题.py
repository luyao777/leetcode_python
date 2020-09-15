#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#

# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x+y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or z == x+y
        return z % math.gcd(x, y) == 0

# @lc code=end

