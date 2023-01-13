#
# @lc app=leetcode.cn id=1719 lang=python3
#
# [1719] 重构一棵树的方案数
#

# @lc code=start
import collections
from sys import maxsize
from typing import List


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)
        n = len(graph)
        root = -1
        for node, neighbours in graph.items():
            if len(neighbours) == n - 1:
                root = node
        
        if root == -1:
            return 0

        ans = 1
        for node, neighbours in graph.items():
            if node == root:
                continue
            cur_deg = len(neighbours)
            parent = -1
            parent_deg = maxsize
            for neighbour in neighbours:
                if cur_deg <= len(graph[neighbour]) < parent_deg:
                    parent = neighbour
                    parent_deg = len(graph[neighbour])
                
            if parent == -1 or any(neighbour != parent and neighbour not in graph[parent] for neighbour in neighbours):
                return 0
            
            if parent_deg == cur_deg:
                ans = 2
        return ans
# @lc code=end

