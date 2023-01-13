#
# @lc app=leetcode.cn id=2076 lang=python3
#
# [2076] 处理含限制条件的好友请求
#

# @lc code=start
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.cnt = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.cnt -= 1

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        ans = []
        for x, y in requests:
            rx, ry = uf.find(x), uf.find(y)
            if rx == ry:
                ans.append(True)
            else:
                flag = True
                for u, v in restrictions:
                    ru, rv = uf.find(u), uf.find(v)
                    if (rx == ru and ry == rv) or (rx == rv and ry == ru):
                        flag = False
                        break
                
                if flag:
                    uf.union(rx, ry)
                    ans.append(True)
                else:
                    ans.append(False)
        return ans
# @lc code=end

