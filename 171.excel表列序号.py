'''
@Author: Yao Lu
@Date: 2019-11-06 16:43:40
@Description: 
'''
#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        count = 0
        sum = 0
        for i in s[::-1]:
            v = ord(i)-ord('A') + 1
            sum += v * pow(26,count)
            count += 1
        return sum
            
        
# @lc code=end

