#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points_len = len(points)
        if points_len <= 1:
            return points_len

        def takeSecond(elem):
            return elem[1]
        points.sort(key=takeSecond)

        shot = points[0][1]
        shot_num = 1
        i = 0
        while(i < points_len):
            if points[i][0] <= shot <= points[i][1]:
                i += 1
                continue
            else:
                shot = points[i][1]
                shot_num += 1
                i += 1
        return shot_num
     
# @lc code=end

