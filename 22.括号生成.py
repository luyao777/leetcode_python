#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]
        for i in range(1, n + 1):
            for p in range(i):
                l1 = dp[p]
                l2 = dp[i - 1 - p]
                for k1 in l1:
                    for k2 in l2:
                        dp[i].append("({0}){1}".format(k1, k2))

        return dp[n]


# @lc code=end
