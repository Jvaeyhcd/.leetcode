#
# @lc app=leetcode.cn id=1928 lang=python
#
# [1928] 规定时间内到达终点的最小花费
#

# @lc code=start
class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        """
        :type maxTime: int
        :type edges: List[List[int]]
        :type passingFees: List[int]
        :rtype: int
        """
        # n = len(passingFees)
        # graph = defaultdict(lambda:defaultdict(lambda:1001))
        # for u, v, time in edges:
        #     graph[u][v] = min(graph[u][v], time)
        #     graph[v][u] = min(graph[v][u], time)
        
        # pq = [(passingFees[0], maxTime, 0)]
        # expored = {0: maxTime}
        # while pq:
        #     fee, time, u = heapq.heappop(pq)
        #     if u == n - 1:
        #         return fee
            
        #     for v, t in graph[u].items():
        #         if t > time:
        #             continue
        #         if v not in expored or time - t > expored[v]:
        #             expored[v] = time - t
        #             heapq.heappush(pq, (fee + passingFees[v], time - t, v))
        
        # return -1
        INF = 0xf3f3f3f3
        n = len(passingFees)
        dp = [[INF] * n for _ in range(maxTime + 1)]
        dp[0][0] = passingFees[0]

        for t in range(1, maxTime + 1):
            for j, i, time in edges:
                if time <= t:
                    dp[t][i] = min(dp[t][i], dp[t - time][j] + passingFees[i])
                    dp[t][j] = min(dp[t][j], dp[t - time][i] + passingFees[j])
        
        ans = min([dp[t][n - 1] for t in range(1, maxTime + 1)])
        return -1 if ans == INF else ans

# @lc code=end

