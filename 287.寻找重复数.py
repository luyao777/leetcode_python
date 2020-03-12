#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        while (left < right):
            mid = (left + right) // 2
            count = 0
            for num in nums:
                if (num <= mid):
                    count += 1
            if (count <= mid):
                left = mid + 1
            else:
                right = mid
        return left


# @lc code=end
