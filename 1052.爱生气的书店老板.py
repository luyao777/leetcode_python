#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    # def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
    def maxSatisfied(self, customers, grumpy, X) -> int:
        # result = 0
        # no_change_profit = sum([customers[j] * (1-grumpy[j]) for j in range(len(customers))])
        # print(no_change_profit)
        # profit = sum([customers[j] * (grumpy[j]) for j in range(0, X)])
        # print(profit)
        # for i in range(1, len(grumpy) - X + 1):
        #     more = -grumpy[i-1] * customers[i-1] + grumpy[i+X-1] * customers[i+X-1]
        #     print(grumpy[i-1], customers[i-1], grumpy[i+X-1], customers[i+X-1])
        #     print(more)
        #     if more > result:
        #         result = more
        # # print(more)

        # result += no_change_profit + profit
        # print(result)
        # return result
        t = 0
        for i in range(len(grumpy)):  #记录下一定满意的顾客数，并把不影响的地方去掉
            if grumpy[i] == 0:
                t += customers[i]
                customers[i] = 0

        n = sum(customers[:X])  #滑动窗口找连续X个的最大值
        m = n
        for i in range(1, len(customers) - X + 1):
            m = m + customers[i + X - 1] - customers[i - 1]
            n = max(m, n)
            #print(n)
        return n + t


# a = Solution()
# customers = [1,0,1,2,1,1,7,5]
# grumpy = [0,1,0,1,0,1,0,1]
# X = 3
# a.maxSatisfied(customers, grumpy, X)
# @lc code=end
