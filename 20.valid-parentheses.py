#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (36.21%)
# Total Accepted:    44.1K
# Total Submissions: 121.8K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False
        stack = []
        p = -1
        for i in range(len(s)):
            if s[i]=='[' or s[i]=='{' or s[i]=='(':
                stack.append(s[i])
                p += 1
                continue
            if (p != -1) and ((s[i]==')' and stack[p] =='(') or (s[i]==']' and stack[p] =='[') or (s[i]=='}' and stack[p] =='{'))  :
                stack.pop()
                p -= 1
                continue
            else:
                return False
        if p == -1:
            return True
        else:
            return False
 

# while(1):
#     a = Solution()
#     b = input('Give the input: ')
#     print(a.isValid(b))
