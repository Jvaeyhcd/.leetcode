#
# @lc app=leetcode.cn id=1157 lang=python3
#
# [1157] 子数组中占绝大多数的元素
#

# @lc code=start
from bisect import bisect
from typing import List


class Node:

    def __init__(self, m:int=0, cnt:int=0):
        self.m = m
        self.cnt = cnt


    def __str__(self):
        return "({0},{1})".format(self.m, self.cnt)
        
    
    def __add__(self, other: 'Node') -> 'Node':
        m = self.m
        cnt = self.cnt
        if self.m == other.m:
            cnt += other.cnt
        elif cnt > other.cnt:
            cnt -= other.cnt
        else:
            m = other.m
            cnt = other.cnt - cnt
        return Node(m, cnt)


class SegTree:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.n = len(arr)
        self.tree = [Node() for _ in range(self.n * 4)]
        self._build(0, self.n - 1, 0)


    def _build(self, l: int, r: int, node: int):
        if l == r:
            self.tree[node] = Node(self.arr[l], 1)
            return
        mid = (l + r) >> 1
        self._build(l, mid, self._left(node))
        self._build(mid + 1, r, self._right(node))
        self._push_up(node)
    

    def _push_up(self, node: int):
        self.tree[node] = self.tree[self._left(node)] + self.tree[self._right(node)]


    def _left(self, node: int):
        return (node << 1) + 1
    

    def _right(self, node: int):
        return (node << 1) + 2
        
    
    def _query(self, L: int, R: int, l: int, r: int, node: int):
        if R < l or L > r:
            return None
        elif L <= l and r <= R:
            return self.tree[node]
        
        mid = (l + r) >> 1
        left = self._query(L, R, l, mid, self._left(node))
        right = self._query(L, R, mid + 1, r, self._right(node))
        if left and right:
            return left + right
        elif left:
            return left
        elif right:
            return right
        return None

    
    def query(self, L: int, R: int):
        return self._query(L, R, 0, self.n - 1, 0)


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.dic = {}
        for i, a in enumerate(arr):
            if a in self.dic:
                self.dic[a].append(i)
            else:
                self.dic[a] = [i]
        self.segtree = SegTree(arr)


    def query(self, left: int, right: int, threshold: int) -> int:
        node = self.segtree.query(left, right)
        if not node: return -1
        k, v = node.m, node.cnt
        if v <= 0:
            return -1
        if bisect(self.dic[k], right) - bisect(self.dic[k], left - 1) >= threshold:
            return k
        return -1
        # print(cnt, left, right)
        



# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
# @lc code=end

solution = MajorityChecker([1,1,2,2,1,1])
solution.query(0,5,4)
solution.query(0,3,3)
solution.query(2,3,2)

m, count = 0, 0
arr = [1, 3, 3, 2, 3]
n = len(arr)
for i in range(n):
    if count == 0:
        m = arr[i]
    if m == arr[i]:
        count += 1
    else:
        count -= 1
# 最后需要验证答案是否符合要求