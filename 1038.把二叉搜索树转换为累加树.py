#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.prevsums = 0
        def dfs(root: TreeNode):
            if not root: return
            dfs(root.right)
            root.val = root.val + self.prevsums
            self.prevsums = root.val
            dfs(root.left)
        
        dfs(root)
        return root

# @lc code=end

