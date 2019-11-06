'''
@Author: Yao Lu
@Date: 2019-11-05 19:27:51
@Description: 杨辉三角
'''

#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            result = []
        elif numRows == 1:
            result = [[1]]
        elif numRows == 2:
            result = [[1], [1, 1]]
        else:
            result = [[1], [1, 1]]
            for i in range(2, numRows):
                cur_list = [1]
                for j in range(1, len(result[i - 1])):
                    cur_list.append(result[i - 1][j] + result[i - 1][j - 1])
                cur_list.append(1)
                result.append(cur_list)
        return result


# @lc code=end
