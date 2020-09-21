#
# @lc app=leetcode.cn id=1552 lang=python3
#
# [1552] 两球之间的磁力
#

# @lc code=start
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 排序，确定上下边界
        position.sort()
        left = min([(position[i+1] - position[i]) for i in range(len(position) - 1)])
        right = position[-1] - position[0]

        def check(diff):
            """检查按照当前值分区的个数是否满足题目要求"""
            count = 0
            i, j = 0, 0
            while j < len(position):
                while j < len(position) and position[j] - position[i] < diff:
                    j += 1
                if j < len(position):
                    count += 1
                i = j 
            return count >= m - 1

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

# @lc code=end

