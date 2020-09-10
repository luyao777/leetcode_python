#
# @lc app=leetcode.cn id=1574 lang=python3
#
# [1574] 删除最短的子数组使剩余数组有序
#

# @lc code=start
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        # 删除尾部元素
        left = 0  # 定义left=0是保证可以留下最开始的arr[0]
        for i in range(1, n):
            if arr[i] >= arr[i - 1]:
                left = i
            else:
                break
        if left == n - 1:
            return 0
        # 删除头部元素
        right = n - 1  # 定义right=n-1是保证可以留下最末尾的arr[n-1]
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                right = i
            else:
                break
        ans = min(n - left + 1, right)
        # 删除中间元素
        i = left
        j = right
        for i in range(left, -1, -1):
            j = right
            if arr[i] <= arr[right]:
                ans = min(ans, right - i - 1)
                break
            while j < n and arr[i] > arr[j]:
                j += 1
            ans = min(ans, j - i - 1)

        return ans
# @lc code=end
