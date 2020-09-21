#
# @lc app=leetcode.cn id=1573 lang=python3
#
# [1573] 分割字符串的方案数
#

# @lc code=start
class Solution:
    def numWays(self, s: str) -> int:
        cal = lambda x: x*(x-1) // 2

        one_index_list = []
        for i in range(len(s)):
            if s[i] == '1': one_index_list.append(i)
        list_len = len(one_index_list)
        if list_len % 3 != 0: return 0
        if list_len == 0:
            result = cal(len(s)-1) % (10**9+7)
        else:
            first_pharse_end = one_index_list[list_len // 3-1]
            second_pharse_first = one_index_list[list_len // 3]
            second_pharse_end = one_index_list[list_len // 3 * 2-1]
            third_pharse_first = one_index_list[list_len // 3 * 2]

            # print(first_pharse_end, second_pharse_first, second_pharse_end, third_pharse_first)

            result = (second_pharse_first - first_pharse_end) * (third_pharse_first - second_pharse_end) % (10**9+7)
        return result

# a = Solution()
# s = '00000000'
# print(a.numWays(s))

# @lc code=end

