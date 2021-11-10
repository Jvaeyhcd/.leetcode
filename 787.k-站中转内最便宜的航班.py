#
# @lc app=leetcode.cn id=787 lang=python
#
# [787] K 站中转内最便宜的航班
#

# @lc code=start
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        INF = 10000 * 101 + 1
        dp = [[INF] * n for _ in range(k + 2)]
        dp[0][src] = 0
        for t in range(1, k + 2):
            for j, i, cost in flights:
                dp[t][i] = min(dp[t][i], dp[t - 1][j] + cost)
        
        ans = min(dp[t][dst] for t in range(1, k + 2))
        return -1 if ans == INF else ans



    # def findCheapestPrice(self, n, flights, src, dst, k):
    #     """
    #     :type n: int
    #     :type flights: List[List[int]]
    #     :type src: int
    #     :type dst: int
    #     :type k: int
    #     :rtype: int
    #     """
    #     INF = 0xf3f3f3f3
    #     # 邻接表
    #     graph = [[] for _ in range(n)]
    #     for f, t, price in flights:
    #         graph[f].append([t, price])
        
    #     # 如果起点与终点不连通
    #     if not self.check(graph, src, dst):
    #         return -1
        
    #     # 使用Dijkstra算法
    #     # 用优先队列选择符合条件的最低价格
    #     # 以price大小进行小根堆的排列
    #     pq = [[0, -1, src]]
    #     while pq:
    #         price, step, u = heapq.heappop(pq)
    #         if u == dst:
    #             return price
    #         for v, cost in graph[u]:
    #             if step + 1 <= k:
    #                 heapq.heappush(pq, [price + cost, step + 1, v])
        
    #     return -1

    # # 检测图中的起点与终点之间是否是连通的
    # def check(self, graph, src, dst):
    #     visited = set()
    #     que = [src]
    #     while que:
    #         u = que.pop(0)
    #         visited.add(u)
    #         for v, _ in graph[u]:
    #             if v not in visited:
    #                 que.append(v)
    #     return (dst in visited)
        
# @lc code=end

