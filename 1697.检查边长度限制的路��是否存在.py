#
# @lc app=leetcode.cn id=1697 lang=python3
#
# [1697] 检查边长度限制的路径是否存在
#

# @lc code=start
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]

    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        i = 0
        ans = [0 for _ in range(len(queries))]
        edgeList.sort(key=lambda x:x[2])

        UF = UnionFind(n)
        for idx, (u, v, w) in sorted(enumerate(queries), key=lambda x:x[1][2]):
            while i < len(edgeList) and edgeList[i][2] < w:
                UF.union(edgeList[i][0], edgeList[i][1])
                i += 1
            ans[idx] = UF.connected(u, v)
        
        return ans

# @lc code=end

