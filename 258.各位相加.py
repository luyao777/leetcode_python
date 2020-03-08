#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    # https://www.zhihu.com/question/30972581/answer/50203344
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return (num - 1) % 9 + 1
# @lc code=end

