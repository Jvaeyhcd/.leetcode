#
# @lc app=leetcode.cn id=743 lang=python
#
# [743] 网络延迟时间
#

# @lc code=start
class Solution(object):

    # SPFA
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        INF = 0xf3f3f3f3
        dist = [INF] * n
        # cnt表示节点入队次数
        cnt = [0] * n
        # 是否在队列
        inque = [False] * n
        # 邻接表
        graph = collections.defaultdict(list)
        for x, y, time in times:
            graph[x - 1].append((y - 1, time))
        
        start = k - 1
        que = collections.deque()
        que.append(start)
        dist[start] = 0
        inque[start] = True

        while que:
            x = que.popleft()
            inque[x] = False
            for y, time in graph[x]:
                d = dist[x] + time
                if d < dist[y]:
                    dist[y] = d
                    inque[y] = True
                    que.append(y)

        ans = max(dist)
        return -1 if ans == INF else ans


    # bellman ford算法
    # def networkDelayTime(self, times, n, k):
    #     """
    #     :type times: List[List[int]]
    #     :type n: int
    #     :type k: int
    #     :rtype: int
    #     """
    #     INF = 0xf3f3f3f3
    #     self.dist = [INF] * (n + 1)
        
    #     def bellman_ford(g, m, n):
    #         # 进行n-1次循环
    #         for _ in range(n - 1):
    #             # 处理全部m条边
    #             for j in range(m):
    #                 # 松弛操作
    #                 if self.dist[g[j][1]] > self.dist[g[j][0]] + g[j][2]:
    #                     self.dist[g[j][1]] = self.dist[g[j][0]] + g[j][2]
                
    #         for i in range(m):
    #             # 这种情况下就存在负权边
    #             if self.dist[g[i][1]] > self.dist[g[i][0]] + g[i][2]:
    #                 return False
    #         return True
        
    #     self.dist[k] = 0
    #     self.dist[0] = 0
    #     if not bellman_ford(times, len(times), n):
    #         return -1
    #     ans = max(self.dist)
    #     return -1 if ans == INF else ans

    # Dijkstra朴素算法（枚举+邻接矩阵）
    # def networkDelayTime(self, times, n, k):
    #     """
    #     :type times: List[List[int]]
    #     :type n: int
    #     :type k: int
    #     :rtype: int
    #     """
    #     MAX = 0xf3f3f3f3
    #     # 构建邻接矩阵
    #     graph = [[MAX] * n for _ in range(n)]
    #     for x, y, time in times:
    #         graph[x - 1][y - 1] = time
        
    #     # dist一维数组记录节点k到其余各个顶点的初始路程
    #     dist = [MAX] * n
    #     dist[k - 1] = 0
    #     # 记录节点是否已经被访问了
    #     visited = [False] * n
    #     for _ in range(n):
    #         x = -1
    #         for y in range(n):
    #             if not visited[y] and (x == -1 or dist[y] < dist[x]):
    #                 x = y
    #         visited[x] = True
    #         for y in range(n):
    #             dist[y] = min(dist[y], dist[x] + graph[x][y])
    #     ans = max(dist)
    #     return -1 if ans == MAX else ans

    # Dijkstra小根堆+邻接表
    # def networkDelayTime(self, times, n, k):
    #     """
    #     :type times: List[List[int]]
    #     :type n: int
    #     :type k: int
    #     :rtype: int
    #     """
    #     INF = 0xf3f3f3f3
    #     graph = [[] for _ in range(n)]
    #     for x, y, time in times:
    #         graph[x - 1].append((y - 1, time))
        
    #     dist = [INF] * n
    #     dist[k - 1] = 0
    #     q = [(0, k - 1)]
    #     while q:
    #         time, x = heapq.heappop(q)
    #         if dist[x] < time:
    #             continue
    #         for y, time in graph[x]:
    #             d = dist[x] + time
    #             if d < dist[y]:
    #                 dist[y] = d
    #                 heapq.heappush(q, (d, y))
        
    #     ans = max(dist)
    #     return -1 if ans == INF else ans


# @lc code=end

