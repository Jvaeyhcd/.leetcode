#
# @lc app=leetcode.cn id=310 lang=python3
#
# [310] 最小高度树
#

# @lc code=start
import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1 and len(edges) == 0:
            return [0]
        # 构建邻接表
        graph = collections.defaultdict(list)
        # 所有节点的入度
        indeg = [0 for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indeg[u] += 1
            indeg[v] += 1
        
        # 由于图是无向图，所以入度为1的节点就是叶子节点
        queue = collections.deque(i for i in range(n) if indeg[i] == 1)
        ans = []
        while queue:
            ans = []
            for _ in range(len(queue)):
                u = queue.popleft()
                # print(u)
                ans.append(u)
                for v in graph[u]:
                    indeg[v] -= 1
                    if indeg[v] == 1:
                        queue.append(v)
        return ans


# @lc code=end

