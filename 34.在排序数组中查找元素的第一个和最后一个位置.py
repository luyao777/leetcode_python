#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        # 空数组的情况
        if end < 0:
            return [-1, -1]
        # 二分查找target落在的位置
        while (start < end):
            if nums[start] == target:
                end = start
                break
            if nums[end] == target:
                start = end
                break
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            if nums[mid] > target:
                end = mid - 1
            if nums[mid] == target:
                start = mid
                end = mid
                break
        # 如果找不到target
        if nums[start] != target:
            return [-1, -1]
        # 找到target，向前向后搜索边界
        while (start > 0 and nums[start - 1] == target):
            start -= 1
        while (end < len(nums) - 1 and nums[end + 1] == target):
            end += 1

        return [start, end]


# @lc code=end
