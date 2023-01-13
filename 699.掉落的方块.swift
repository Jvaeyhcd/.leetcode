/*
 * @lc app=leetcode.cn id=699 lang=swift
 *
 * [699] 掉落的方块
 */

// @lc code=start
class SegTreeNode {
    var left: SegTreeNode?
    var right: SegTreeNode?
    var val: Int
    var l: Int
    var r: Int
    var lazzy: Int
    
    init(_ l: Int, _ r: Int) {
        self.left = nil
        self.right = nil
        self.val = 0
        self.l = l
        self.r = r
        self.lazzy = 0
    }
}

class Segtree {
    var root: SegTreeNode

    init() {
        self.root = SegTreeNode(0, 1000000000)
    }

    func _pushUp(_ node: inout SegTreeNode) {
        node.val = max(node.left!.val, node.right!.val)
    }

    func _pushDown(_ node: inout SegTreeNode) {
        let l = node.l
        let r = node.r
        let mid = (l + r) >> 1
        if node.left == nil {
            node.left = SegTreeNode(l, mid)
        }
        if node.right == nil {
            node.right = SegTreeNode(mid + 1, r)
        }
        if node.lazzy > 0 {
            node.left!.lazzy = node.lazzy
            node.right!.lazzy = node.lazzy
            node.left!.val = node.val
            node.right!.val = node.val
            node.lazzy = 0
        }
    }

    func _query(_ L: Int, _ R: Int, _ node: inout SegTreeNode) -> Int {
        if L > node.r || R < node.l {
            return 0
        } else if (L <= node.l && node.r <= R) {
            return node.val
        }
        self._pushDown(&node)
        return max(self._query(L, R, &(node.left!)), self._query(L, R, &(node.right!)))
    }

    func _update(_ L: Int, _ R: Int, _ node: inout SegTreeNode, _ val: Int) {
        if L <= node.l && node.r <= R {
            node.val = val
            node.lazzy = val
            return
        }
        self._pushDown(&node)
        let mid = (node.l + node.r) >> 1
        if L <= mid {
            self._update(L, R, &(node.left!), val)
        }
        if R > mid {
            self._update(L, R, &(node.right!), val)
        }
        self._pushUp(&node)
    }

    func query(_ L: Int, _ R: Int) -> Int {
        return self._query(L, R, &(self.root))
    }

    func update(_ L: Int, _ R: Int, _ val: Int) {
        self._update(L, R, &(self.root), val)
    }
}


class Solution {
    func fallingSquares(_ positions: [[Int]]) -> [Int] {
        var ans = [Int]()
        let segtree = Segtree()
        var height = 0
        for poistion in positions {
            let l = poistion[0]
            let w = poistion[1]
            let r = l + w - 1
            let h = segtree.query(l, r)
            segtree.update(l, r, w + h)
            if height < h + w {
                height = h + w
            }
            ans.append(height)
        }
        return ans
    }
}
// @lc code=end

let solution = Solution()
var positions = [[100, 100], [200, 100]]
positions = [[1, 2], [2, 3], [6, 1]]
print(solution.fallingSquares(positions))