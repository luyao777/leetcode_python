#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == "":
            return -1
        char_dict = {}
        for s_i in s:
            if s_i not in char_dict.keys():
                char_dict[s_i] = 1
            else:
                char_dict[s_i] += 1
        no_flag = True
        for key in char_dict.keys():
            if char_dict[key] == 1:
                no_flag = False
                break
        if no_flag:
            return -1
        for i in range(len(s)):
            if s[i] == key:
                return i
# @lc code=end

