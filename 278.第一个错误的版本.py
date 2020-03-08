#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start_num = 1
        check_num = n
        while(start_num != check_num):
            check_num = (n + start_num) // 2
            if isBadVersion(check_num):
                n = check_num
            else:
                start_num = check_num + 1
        return check_num
        
# @lc code=end

