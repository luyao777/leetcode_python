class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 1 or min(A) == max(A): return 1
        dp = [1 for _ in range(len(A))]
        for i in range(1, len(A)-1):
            if A[i-1] > A[i] < A[i+1] or A[i-1] < A[i] > A[i+1]:
                dp[i] = dp[i-1] + 1
        return max(dp)+1
