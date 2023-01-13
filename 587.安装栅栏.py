#
# @lc app=leetcode.cn id=587 lang=python3
#
# [587] 安装栅栏
#

# @lc code=start
from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort()
        n = len(trees)
        hull = []
        for tree in trees:
            while len(hull) > 1 and self.orientation(hull[-2], hull[-1], tree) > 0:
                hull.pop()
            hull.append(tree)
        hull.pop()
        for i in range(n - 1, -1, -1):
            while len(hull) > 1 and self.orientation(hull[-2], hull[-1], trees[i]) > 0:
                hull.pop()
            hull.append(trees[i])
        
        res = []
        for tree in set((x, y) for x, y in hull):
            res.append([tree[0], tree[1]])
        return res

    def orientation(self, p1: List[int], p2: List[int], p3: List[int]) -> int:
        return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
# @lc code=end

