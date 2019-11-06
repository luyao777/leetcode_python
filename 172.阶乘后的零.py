'''
@Author: Yao Lu
@Date: 2019-11-06 16:48:29
@Description: 
'''

#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#


# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        
        while n >= 5:
            res += n // 5
            n //= 5
        
        return res

                    
# @lc code=end

# Solution().trailingZeroes(3)