#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if s1_len > s2_len:
            return False
        s1_dict = {}
        s2_dict = {}
        for i in range(s1_len):
            if s1[i] not in s1_dict.keys():
                s1_dict[s1[i]] = 1
            else:
                s1_dict[s1[i]] += 1

        for i in range(s1_len):
            if s2[i] not in s2_dict.keys():
                s2_dict[s2[i]] = 1
            else:
                s2_dict[s2[i]] += 1

        if s1_dict == s2_dict:
            return True

        for i in range(s1_len, s2_len):
            s2_dict[s2[i-s1_len]] -= 1
            if s2_dict[s2[i-s1_len]] == 0:
                del s2_dict[s2[i-s1_len]]
            if s2[i] not in s2_dict.keys():
                s2_dict[s2[i]] = 1
            else:
                s2_dict[s2[i]] += 1
            if s1_dict == s2_dict:
                return True
        
        return False    

# @lc code=end

