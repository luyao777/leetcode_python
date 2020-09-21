#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#

# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        from queue import PriorityQueue
        cal = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])  # 计算曼哈顿距离的函数

        pq = PriorityQueue()  # 来，复习一下优先队列的API | PS:要是卡常，就换成"配对堆"
        visit = set([i for i in range(len(points))])  # 待访问的节点集
        res = 0

        pq.put((0, 0))  # (distance, point_id)  # Prim算法从任何一个节点出发都是一样的，这里从0点开始
        while visit:  # 当没有访问完所有节点 | 其它语言的coder请把这行理解成 => while(visit.length() > 0){...}
            dis, now = pq.get()  # 获取优先队列中最小的项 => (到扩展集中某最近点的距离，某最近点的序号)
            if now not in visit:  # 已访问过的直接跳过
                continue
            visit.remove(now)  # 随手剪枝，移除出待访问的节点集
            res += dis
            for i in visit:  # 构建扩展集，就是把当前点对所有未访问点的距离都求一遍
                # 以距离为cost丢进优先队列排序就好，想不清明白其它题解费劲构建边结构干啥...
                pq.put((cal(points[now], points[i]), i))

        return res

# @lc code=end

