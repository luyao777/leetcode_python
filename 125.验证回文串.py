'''
@Author: Yao Lu
@Date: 2019-11-06 14:03:57
@Description: 
'''
#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        s = s.lower()
        string = ""
        for letter in s:
            if ('a'<=letter<='z') or ('0'<=letter<='9'):
                string += letter
        rev_string = string[::-1]
        if string == rev_string:
            return True
        else:
            return False
        
# @lc code=end

