#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.61%)
# Total Accepted:    48.7K
# Total Submissions: 154K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        comstr = ""
        if strs == []:
            return comstr
        for i in range(len(strs[0])):
            for j in strs:
                try:
                    if j[i] == strs[0][i]:
                        continue
                    else:
                        return comstr
                except IndexError:
                    return comstr
            comstr += strs[0][i]
        return comstr


# a = Solution()
# b = [""]
# print(a.longestCommonPrefix(b))



        
