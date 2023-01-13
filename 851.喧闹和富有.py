#
# @lc app=leetcode.cn id=851 lang=python3
#
# [851] 喧闹和富有
#

# @lc code=start
from typing import List
import collections

# 拓扑排序
# class Solution:
#     def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
#         n = len(quiet)
#         # 邻接表
#         graph = collections.defaultdict(list)
#         # 入度
#         indeg = [0] * n
#         for p1, p2 in richer:
#             graph[p1].append(p2)
#             indeg[p2] += 1
        
#         ans = [i for i in range(n)]
#         queue = [i for i, deg in enumerate(indeg) if deg == 0]
#         while queue:
#             x = queue.pop(0)
#             for y in graph[x]:
#                 if quiet[ans[x]] < quiet[ans[y]]:
#                     ans[y] = ans[x]
#                 indeg[y] -= 1
#                 if indeg[y] == 0:
#                     queue.append(y)
#         return ans

# 深度优先搜索
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = collections.defaultdict(list)
        for x, y in richer:
            graph[y].append(x)
        
        ans = [-1] * n
        def dfs(x: int):
            if ans[x] != -1:
                return
            ans[x] = x
            for y in graph[x]:
                dfs(y)
                if quiet[ans[y]] < quiet[ans[x]]:
                    ans[x] = ans[y]
        
        for i in range(n):
            dfs(i)
        return ans


# @lc code=end

