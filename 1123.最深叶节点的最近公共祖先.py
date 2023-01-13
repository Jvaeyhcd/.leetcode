#
# @lc app=leetcode.cn id=1123 lang=python3
#
# [1123] 最深叶节点的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        arr = []
        queue = [root]
        nodes = []
        while queue:
            nodes = []
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return self.lowestCommonAncestor(root, nodes)

    def lowestCommonAncestor(self, root: TreeNode, nodes: List[TreeNode]) -> 'TreeNode':
        if not root:
            return None
        for node in nodes:
            if node.val == root.val:
                return root
        
        left = self.lowestCommonAncestor(root.left, nodes)
        right = self.lowestCommonAncestor(root.right, nodes)
        if left and right:
            return root
        return left if left else right
# @lc code=end