#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            if num not in nums_dict.keys():
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        heap = []

        for key in nums_dict.keys():
            heappush(heap, [-nums_dict[key], key])

        result = []
        for _ in range(k):
            result.append(heappop(heap)[1])

        return result

# @lc code=end

