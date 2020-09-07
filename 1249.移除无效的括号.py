#
# @lc app=leetcode.cn id=1249 lang=python3
#
# [1249] 移除无效的括号
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = ""
        kuo_left = []
        kuo_right = []
        for i in range(len(s)):
            if s[i] == '(':
                kuo_left.append(i)
            elif s[i] == ')':
                if len(kuo_left) > 0:
                    kuo_left.pop()
                else:
                    kuo_right.append(i)
        # print(delete)
        for i in range(len(s)):
            if s[i] == ')' and i not in kuo_right:
                result += s[i]
            if s[i] == '(' and i not in kuo_left:
                result += s[i]
            if s[i] != '(' and s[i] != ')':
                result += s[i]
        return result

        
# @lc code=end

