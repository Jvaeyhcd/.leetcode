#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#

# @lc code=start
import collections
import copy
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)
        for k in graph.keys():
            graph[k].sort()

        def dfs(g: dict, path: List[str]) -> List[str]:
            if not g[path[-1]]:
                if not any(g.values()):
                    return path
                else:
                    return []
            for t in g[path[-1]]:
                gg = copy.deepcopy(g)
                gg[path[-1]].remove(t)
                res = dfs(gg, path + [t])
                if res:
                    return res
            return []
        
        return dfs(graph, ["JFK"])
# @lc code=end

