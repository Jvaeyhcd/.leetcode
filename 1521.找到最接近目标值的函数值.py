#
# @lc app=leetcode.cn id=1521 lang=python3
#
# [1521] 找到最接近目标值的函数值
#

# @lc code=start
from typing import List


class SegTree:

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0 for _ in range(self.n << 2)]


    def _ls(self, node: int) -> int:
        return (node << 1) + 1

    
    def _rs(self, node: int) -> int:
        return (node << 1) + 2


    def _push_up(self, node: int):
        self.tree[node] = self.tree[self._ls(node)] & self.tree[self._rs(node)]

    
    def _build(self, l: int, r: int, node: int):
        if l == r:
            self.tree[node] = self.arr[l]
            return
        mid = (l + r) >> 1
        self._build(l, mid, self._ls(node))
        self._build(mid + 1, r, self._rs(node))
        self._push_up(node)


    def _query(self, L: int, R: int, l: int, r: int, node: int) -> int:
        if R < l or L > r:
            return 0
        elif L <= l and r <= R:
            return self.tree[node]
        
        mid = (l + r) >> 1
        return self._query(L, R, l, mid, self._ls(node)) & self._query(L, R, mid + 1, r, self._rs(node))


    def query(self, l: int, r: int) -> int:
        if r < l:
            return -10**9
        return self._query(l, r, 0, self.n - 1, 0)


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:





# @lc code=end

