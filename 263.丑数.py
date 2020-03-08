#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        div_nums = [2, 3, 5]
        for div_num in div_nums:
            while num % div_num == 0:
                num /= div_num
        if num == 1:
            return True
        else:
            return False
        
# @lc code=end

