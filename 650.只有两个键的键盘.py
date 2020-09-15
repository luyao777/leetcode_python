#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        zhi_nums = []
        for i in range(2, n+1):
            if n == 1:
                break
            while(n % i == 0):
                zhi_nums.append(i)
                n = n // i
        zhi_nums.sort(reverse=True)
        total_op = 0
        for num in zhi_nums:
            total_op += num
        return total_op
  
# @lc code=end

