#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#


# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def perm(res_nums, cur_result):
            if len(res_nums) == 1:
                result.append(cur_result + res_nums)
                return
            for i in range(len(res_nums)):
                if i < len(res_nums) - 1 and res_nums[i] == res_nums[i + 1]:
                    continue
                perm(res_nums[:i] + res_nums[i + 1:],
                     cur_result + [res_nums[i]])

        perm(nums, [])

        return result


# @lc code=end
