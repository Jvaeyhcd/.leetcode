#
# @lc app=leetcode.cn id=815 lang=python
#
# [815] 公交路线
#

# @lc code=start
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0
        # 公交路线的个数
        n = len(routes)
        # 根据公交路线构建图，edge[i][j]表示路线i与路线j是否相通
        edge = [[False] * n for _ in range(n)]
        # 记录每个站点的公交车路线号
        rec = collections.defaultdict(list)
        for i in range(n):
            for site in routes[i]:
                lis = rec[site]
                for j in lis:
                    edge[i][j] = edge[j][i] = True
                lis.append(i)
                rec[site] = lis
        
        # 经过某条公交车的换成次数
        dis = [-1] * n
        que = collections.deque()
        for bus in rec[source]:
            dis[bus] = 1
            que.append(bus)
        
        while que:
            x = que.popleft()
            for y in range(n):
                if edge[x][y] and dis[y] == -1:
                    dis[y] = dis[x] + 1
                    que.append(y)
        
        ret = float('inf')
        for bus in rec[target]:
            if dis[bus] != -1:
                ret = min(ret, dis[bus])
        
        return -1 if ret == float('inf') else ret
# @lc code=end

