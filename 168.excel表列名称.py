'''
@Author: Yao Lu
@Date: 2019-11-06 15:57:16
@Description: 
'''
#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        ascii_list = []
        while n > 26:
            res = n % 26
            if res == 0:
                res = 25
                n = n // 26 - 1
            else:
                res -= 1
                n = n // 26
            ascii_list.append(res)
        ascii_list.append(n-1)
        ascii_list.reverse()
        result = ""
        for i in ascii_list:
            result += chr(i + ord('A'))
        return result
        
# @lc code=end

