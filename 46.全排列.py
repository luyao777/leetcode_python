#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def perm(res_nums, cur_result):
            if len(res_nums) == 1:
                result.append(cur_result + res_nums)
                return
            for i in range(len(res_nums)):
                perm(res_nums[:i]+res_nums[i+1:], cur_result + [res_nums[i]])

        perm(nums, [])

        return result


# @lc code=end
