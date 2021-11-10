#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def dfs(root: TreeNode, low: int, high: int) -> int:
            if not root: return 0
            return dfs(root.left, low, high) + dfs(root.right, low, high) + (root.val if low <= root.val <= high else 0)
        
        return dfs(root, low, high)
# @lc code=end

