#
# @lc app=leetcode.cn id=699 lang=python3
#
# [699] 掉落的方块
#

from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        segtree = SegTree()
        ans = []
        height = 0
        for l, w in positions:
            r = l + w - 1
            h = segtree.query(l, r)
            segtree.update(l, r, h + w)
            height = max(w + h, height)
            ans.append(height)

        print(segtree.query(1, 6))
        return ans
        
class SegTreeNode:
    
    def __init__(self, l: int, r: int):
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.val = 0
        self.lazy = 0
        
        

class SegTree:
    
    def __init__(self):
        self.root = SegTreeNode(0, int(1e9 + 1))
        
        
    def _push_up(self, node: SegTreeNode):
        node.val = max(node.left.val, node.right.val)
        
        
    def _push_down(self, node: SegTreeNode):
        l, r = node.l, node.r
        mid = (l + r) >> 1
        if not node.left:
            node.left = SegTreeNode(l, mid)
        if not node.right:
            node.right = SegTreeNode(mid + 1, r)
        if node.lazy:
            node.left.lazy = node.lazy
            node.right.lazy = node.lazy
            node.left.val = node.val
            node.right.val = node.val
            node.lazy = 0
            
            
    def _query(self, L: int, R: int, node: SegTreeNode):
        l, r = node.l, node.r
        if L > r or R < l:
            return 0
        elif L <= l and r <= R:
            return node.val
        
        self._push_down(node)
        ans = 0
        mid = (l + r) >> 1
        if L <= mid:
            ans = max(ans, self._query(L, R, node.left))
        if R > mid:
            ans = max(ans, self._query(L, R, node.right))
        self._push_up(node)
        return ans
    
    
    def _update(self, L: int, R: int, val: int, node: SegTreeNode):
        l, r = node.l, node.r
        if L <= l and r <= R:
            node.val = val
            node.lazy = val
            return
        
        self._push_down(node)
        mid = (l + r) >> 1
        if L <= mid:
            self._update(L, R, val, node.left)
        if R > mid:
            self._update(L, R, val, node.right)
        self._push_up(node)
        
        
    def query(self, L: int, R: int):
        return self._query(L, R, self.root)
    
    
    def update(self, L: int, R: int, val: int):
        self._update(L, R, val, self.root)

# @lc code=end

solution = Solution()
positions = [[100,100],[200,100]]
positions = [[9,7],[1,9]]
positions = [[1, 2], [2, 3], [6, 1]]
print(solution.fallingSquares(positions))