#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                value = self.cache[i][1]
                new_data = self.cache.pop(i)
                self.put(*new_data)
                return value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.cache[-1][1] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.pop(0)
            self.cache.append([key, value])




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

