#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#

# @lc code=start
class UF:
    def __init__(self, n):
        self.parents = defaultdict(int)
        for i in range(n):
            self.parents[i] = i

    def find(self, x):
        while x != self.parents[x]:
            x = self.parents[x]
        return x

    def connect(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        if self.find(p) == self.find(q):
            return
        self.parents[self.find(p)] = self.find(q)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 1:
            return 0
        dic = defaultdict(int)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dic[(i, j)] = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])
        res = sorted(dic.items(), key=lambda item:item[1]) # 对字典按边权值排序
        sumn = 0
        uf = UF(len(points))
        tmp = 0

        for i in range(len(res)):
            t1, t2 = res[i]
            x, y = t1
            if uf.find(x) != uf.find(y):  # 若祖先节点不相同， 则加入。
                tmp += 1
                sumn += t2
                if tmp == len(points)-1:  # 所有边都已加入， 最小生成树完成。
                    return sumn
                uf.union(x, y)

# @lc code=end

