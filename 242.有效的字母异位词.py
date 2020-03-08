#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for i in s:
            if i not in dict_s.keys():
                dict_s[i] = 1
            else:
                dict_s[i] += 1
        for i in t:
            if i not in dict_s.keys():
                return False
            else:
                dict_s[i] -= 1
                if dict_s[i] == 0:
                    del dict_s[i]
        if dict_s == {}:
            return True
        else:
            return False        
            
# @lc code=end

