#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = []
        heapq.heappush(heap, 1)

        hashmap = set()
        hashmap.add(1)

        curr_ugly = 1
        for _ in range(n):
            curr_ugly = heapq.heappop(heap) #pop堆顶
            # print(heap)
            for p in primes:
                new_ugly = curr_ugly * p
                if new_ugly not in hashmap:
                    hashmap.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
            # print(heap)
        return curr_ugly

        
# @lc code=end

