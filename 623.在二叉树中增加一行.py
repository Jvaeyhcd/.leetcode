#
# @lc app=leetcode.cn id=623 lang=python3
#
# [623] 在二叉树中增加一行
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            n = TreeNode(val)
            n.left = root
            return n
        self.insert(val, root, 1, depth)
        return root

    
    def insert(self, val: int, node: TreeNode, depth: int, n: int):
        if not node:
            return
        if depth == n - 1:
            t = node.left
            node.left = TreeNode(val)
            node.left.left = t
            t = node.right
            node.right = TreeNode(val)
            node.right.right = t
        else:
            self.insert(val, node.left, depth + 1, n)
            self.insert(val, node.right, depth + 1, n)

# @lc code=end

