#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (46.15%)
# Total Accepted:    15.7K
# Total Submissions: 34.1K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 
# 输入为非空字符串且只包含数字 1 和 0。
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
#
class Solution:
    def addBinary(self, a, b):
        result = str(int(a) + int(b))
        ext = 0
        for i in range(len(result)-1,-1,-1):
            if result[i] == '2':
                if ext == 1:
                    result = result[:i] + '1' + result[i+1:]
                else:
                    result = result[:i] + '0' + result[i+1:]
                ext = 1
            elif result[i] == '1':
                if ext == 1:
                    result = result[:i] + '0' + result[i+1:]
                else:
                    ext = 0
            else:
                if ext == 1:
                    result = result[:i] + '1' + result[i+1:]
                    ext = 0
        if ext == 1:
            result = '1' + result
        return result
            

# print(Solution().addBinary('1010','1011'))

