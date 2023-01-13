#
# @lc app=leetcode.cn id=715 lang=python3
#
# [715] Range 模块
#

# @lc code=start
import collections


class Node:

    def __init__(self, l: int = 0, r: int = 0):
        self.l = l
        self.r = r
        self.left = None
        self.right = None
        self.tracked = False
        self.lazy = 0

MAX = int(1e9+1)

class RangeModule:

    def __init__(self):
        self.root = Node(0, MAX)


    def _push_up(self, root: Node):
        root.tracked = root.left and root.left.tracked and root.right and root.right.tracked
    

    def _push_down(self, root: Node):
        l, r = root.l, root.r
        mid = (l + r) >> 1
        if not root.left:
            root.left = Node(l, mid)
        if not root.right:
            root.right = Node(mid + 1, r)
        if root.lazy:
            root.left.lazy = root.lazy
            root.right.lazy = root.lazy
            root.left.tracked = root.tracked
            root.right.tracked = root.tracked
            root.lazy = 0


    def _update_range(self, L: int, R: int, tracked: bool, root: Node):
        start, end = root.l, root.r
        if L <= start and end <= R:
            root.tracked = tracked
            root.lazy = True
            return
        
        mid = (start + end) >> 1
        self._push_down(root)
        if L <= mid:
            self._update_range(L, R, tracked, root.left)
        if R > mid:
            self._update_range(L, R, tracked, root.right)
        
        self._push_up(root)


    def _query(self, L: int, R: int, root: Node) -> bool:
        start, end = root.l, root.r
        if R < start or end < L:
            return True
        if L <= start and end <= R:
            return root.tracked
        
        self._push_down(root)
        return self._query(L, R, root.left) and self._query(L, R, root.right)



    def addRange(self, left: int, right: int) -> None:
        self._update_range(left, right - 1, True, self.root)


    def queryRange(self, left: int, right: int) -> bool:
        return self._query(left, right - 1, self.root)


    def removeRange(self, left: int, right: int) -> None:
        self._update_range(left, right - 1, False, self.root)



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
# @lc code=end

