class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs_bak = strs.copy()
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for str_i in strs:
            num_1, num_0 = str_i.count('1'), str_i.count('0')

            for i in range(n, num_1 - 1, -1):
                for j in range(m, num_0 - 1, -1):
                    dp[j][i] = max(1 + dp[j - num_0][i - num_1], dp[j][i])
        return dp[m][n]
