#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        p = 1
        while (p < len(intervals)):
            if intervals[p][0] >= intervals[
                    p - 1][0] and intervals[p][0] <= intervals[p - 1][1]:
                if intervals[p][1] <= intervals[p - 1][1]:
                    intervals.remove(intervals[p])
                else:
                    intervals[p - 1] = [intervals[p - 1][0], intervals[p][1]]
                    intervals.remove(intervals[p])
            else:
                p += 1
        return intervals


# @lc code=end
