#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while(n > 1):
            noun = n % 2
            n = n // 2
            if noun == 1:
                return False
        return True

# @lc code=end

