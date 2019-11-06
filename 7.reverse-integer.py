#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (31.40%)
# Total Accepted:    82K
# Total Submissions: 260K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        if x_str[0] == '-':
            x_str = x_str[1:]
            x_reverse_str = x_str[::-1]
            x_reverse_long = int(x_reverse_str)
            if x_reverse_long > 2 ** 31:
                return 0
            else:
                return -x_reverse_long
        else:
            x_reverse_str = x_str[::-1]
            x_reverse_long = int(x_reverse_str)
            if x_reverse_long > 2 ** 31 -1:
                return 0
            else:
                return x_reverse_long
        
