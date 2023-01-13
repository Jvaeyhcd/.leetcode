#
# @lc app=leetcode.cn id=1916 lang=python3
#
# [1916] 统计为蚁群构筑房间的不同顺序
#

# @lc code=start
import collections
from math import comb
from typing import List


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 1_000_000_007

        g = collections.defaultdict(set)
        for u, v in enumerate(prevRoom):
            g[v].add(u)
        
        def dfs(u: int):
            nodes, ans = 0, 1
            for v in g[u]:
                nodes_, ans_ = dfs(v)
                nodes += nodes_
                ans = (ans * comb(nodes, nodes_) * ans_) % MOD

            return nodes + 1, ans
        
        return dfs(0)[1]

                

# @lc code=end

