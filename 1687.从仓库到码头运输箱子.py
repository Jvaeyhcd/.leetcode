#
# @lc app=leetcode.cn id=1687 lang=python3
#
# [1687] 从仓库到码头运输箱子
#

# @lc code=start
from typing import List


class SegTree:

    def __init__(self, arr: List[List[int]]):
        self.arr = arr
        self.n = len(arr)
        self.ports = [[] for _ in range(self.n << 2)]
        self.weights = [0 for _ in range(self.n << 2)]
        self._build(0, self.n - 1, 0)


    def _ls(self, node: int) -> int:
        return (node << 1) + 1

    
    def _rs(self, node: int) -> int:
        return (node << 1) + 2

    
    def _push_up(self, node: int):
        self.ports[node] = []
        left_ports = self.ports[self._ls(node)]
        right_ports = self.ports[self._rs(node)]
        if left_ports and right_ports:
            if left_ports[-1] == right_ports[0]:
                self.ports[node] = left_ports + right_ports[1:]
            else:
                self.ports[node] = left_ports + right_ports
        elif left_ports:
            self.ports[node] = left_ports
        elif right_ports:
            self.ports[node] = right_ports
        self.weights[node] = self.weights[self._ls(node)] + self.weights[self._rs(node)]

    
    def _build(self, l: int, r: int, node: int):
        if l == r:
            self.ports[node] = [self.arr[l][0]]
            self.weights[node] = self.arr[l][1]
            return
        mid = (l + r) >> 1
        self._build(l, mid, self._ls(node))
        self._build(mid + 1, r, self._rs(node))
        self._push_up(node)


    def query_weight(self, L: int, R: int, l: int, r: int, node: int) -> int:
        if L > r or R < l:
            return 0
        elif L <= l and r <= R:
            return self.weights[node]
        
        mid = (l + r) >> 1
        ans = 0
        if mid >= L:
            ans += self.query_weight(L, R, l, mid, self._ls(node))
        if mid < R:
            ans += self.query_weight(L, R, mid + 1, r, self._rs(node))
        return ans


    def query_port(self, L: int, R: int, l: int, r: int, node: int):
        if L > r or R < l:
            return set()
        elif L <= l and r <= R:
            return self.ports[node]
        
        mid = (l + r) >> 1
        ans = []
        if mid >= L:
            ans += self.query_port(L, R, l, mid, self._ls(node))
        if mid < R:
            ans += self.query_port(L, R, mid + 1, r, self._rs(node))
        return ans

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        segtree = SegTree(boxes)
        
        
# @lc code=end

solution = Solution()
boxes = [[1,1],[2,1],[1,1]]
portsCount = 2
maxBoxes = 3
maxWeight = 3

boxes = [[2,4],[2,3],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]]
portsCount = 5
maxBoxes = 5
maxWeight = 7

print(solution.boxDelivering(boxes, portsCount, maxBoxes, maxWeight))