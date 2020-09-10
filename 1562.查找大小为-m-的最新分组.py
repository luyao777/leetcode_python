#
# @lc app=leetcode.cn id=1562 lang=python3
#
# [1562] 查找大小为 M 的最新分组
#

# @lc code=start
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        lenToCnt = collections.defaultdict(int)
        iToLen = {}
        res = -1
        for index, x in enumerate(arr):
            # 转成以0为起点的下标
            i = x - 1
            # 原来的左侧和右侧的连续1的长度
            left = 0
            right = 0
            # 新的连续1的起点和终点下标, 初始化为当前下标
            start = i
            end = i
            if i - 1 >= 0 and i - 1 in iToLen:
                # 更新左侧长度和起点下标
                left = iToLen[i - 1]
                start -= left
            if i + 1 < n and i + 1 in iToLen:
                # 更新右侧长度和终点下标
                right = iToLen[i + 1]
                end += right
            newlen = left + right + 1
            # 更新iToLen字典, 只需要更新两个边界即可
            iToLen[start] = newlen
            iToLen[end] = newlen
            # 更新lenToCnt字典, 减去旧长度的值, 加上新长度的值
            lenToCnt[left] -= left
            lenToCnt[right] -= right
            lenToCnt[newlen] += newlen
            if lenToCnt[m] > 0:
                # 如果仍有连续1长度为m的部分, 更新最终结果为当前arr下标+1
                res = index + 1
        return res


        # def check(state, m):
        #     sum_num = 0
        #     for state_i in state:
        #         if state_i == 1:
        #             sum_num += 1
        #         else:
        #             if sum_num == m:
        #                 return True
        #             sum_num = 0
        #     if sum_num == m:
        #         return True
        #     else:
        #         return False

        # state = [0 for _ in range(len(arr)+1)]

        # result = 0
        # for i, num in enumerate(arr):
        #     state[num] = 1
        #     if check(state, m):
        #         result = i + 1

        # if result == 0:
        #     return -1
        # else:
        #     return result
# @lc code=end

