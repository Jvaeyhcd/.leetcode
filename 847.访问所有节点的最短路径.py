#
# @lc app=leetcode.cn id=847 lang=python
#
# [847] 访问所有节点的最短路径
#

# @lc code=start
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)

        queue = collections.deque((i, 1 << i, 0) for i in range(n))
        vis = {(i, i << i) for i in range(n)}

        while queue:
            u, mask, dist = queue.popleft()
            if mask == (1 << n) - 1:
                return dist
            
            for x in graph[u]:
                next_mask = mask | (1 << x)
                if (x, next_mask) not in vis:
                    queue.append((x, next_mask, dist + 1))
                    vis.add((x, next_mask))
        
        return -1
# @lc code=end

