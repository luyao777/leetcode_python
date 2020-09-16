#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        if s == "":
            return s
        s = s.strip().split(' ')[::-1]
        if len(s) == 1:
            return s[0].strip()
        r = s[0].strip()
        for s_i in s[1:]:
            if s_i == "":
                continue
            r += ' '+s_i.strip()
        return r

# @lc code=end

