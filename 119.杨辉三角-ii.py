'''
@Author: Yao Lu
@Date: 2019-11-05 19:42:14
@Description: 杨辉三角 II
'''
#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = [1]
        for i in range(1, rowIndex + 1):
            r.insert(0, 0)
            # 因为i行的数据长度为i+1, 所以j+1不会越界, 并且最后一个1不会被修改.
            for j in range(i):
                r[j] = r[j] + r[j + 1]
        return r
        
# @lc code=end

