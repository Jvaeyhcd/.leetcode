#
# @lc app=leetcode.cn id=1008 lang=python3
#
# [1008] 前序遍历构造二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        inorder = sorted(preorder)

        def build(stop: TreeNode):
            if inorder and inorder[0] != stop:
                root = TreeNode(preorder.pop(0))
                root.left = build(root.val)
                inorder.pop(0)
                root.right = build(stop)
                return root
        
        return build(None)
# @lc code=end

