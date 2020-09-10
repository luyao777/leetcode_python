#
# @lc app=leetcode.cn id=1578 lang=python3
#
# [1578] 避免重复字母的最小删除成本
#

# @lc code=start
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        total_cost = 0
        i = 0
        len_s = len(s)
        while(i < len_s-1):
            if s[i] == s[i+1]:
                j = i + 1
                while(j < len_s-1 and s[j] == s[j+1]):
                    j += 1
                total_cost += sum(cost[i:j+1]) - max(cost[i:j+1])
                # print(i, j+1)
                i = j
            i += 1
        return total_cost
# @lc code=end

