#
# @lc app=leetcode.cn id=2322 lang=python3
#
# [2322] 从树中删除边的最小分数
#

# @lc code=start
from itertools import combinations
from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        xors, ins, outs = [0] * n, [0] * n, [0] * n
        t = 0
        def dfs(x: int, pa: int):
            nonlocal t
            t += 1
            ins[x] = t
            xors[x] = nums[x]
            for y in g[x]:
                if y != pa:
                    dfs(y, x)
                    xors[x] ^= xors[y]
            outs[x] = t

        dfs(0, -1)
        def is_parent(x: int, y: int) -> bool:
            return ins[x] <= ins[y] <= outs[x]

        for e in edges:
            if not is_parent(e[0], e[1]):
                e[0], e[1] = e[1], e[0]

        ans = 0xf3f3f3f3
        for (x1, y1), (x2, y2) in combinations(edges, 2):
            if is_parent(y1, x2):
                x, y, z = xors[y2], xors[y1] ^ xors[y2], xors[0] ^ xors[y1]
            elif is_parent(y2, x1):
                x, y, z = xors[y1], xors[y1] ^ xors[y2], xors[0] ^ xors[y2]
            else:
                x, y, z = xors[y1], xors[y2], xors[0] ^ xors[y1] ^ xors[y2]
            ans = min(ans, max(x, y, z) - min(x, y, z))
            if ans == 0: return ans
        return ans
# @lc code=end

