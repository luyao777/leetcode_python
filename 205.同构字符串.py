'''
@Author: Yao Lu
@Date: 2019-11-07 16:00:39
@Description: 
'''
#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letter_dict = {}
        value_list = []
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in letter_dict.keys():
                if t[i] not in value_list:
                    letter_dict[s[i]] = set(t[i])
                    value_list.append(t[i])
                else:
                    return False

            else:
                letter_dict[s[i]].add(t[i])

        for i in letter_dict.keys():
            if len(letter_dict[i]) != 1:
                return False
        return True        
        
        

        
# @lc code=end
