#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float('inf')
        
        # 遍历返回经过node的单边分支最大和
        def dfs(node: TreeNode):
            if not node: return 0

            # 计算左边最大分支值，左边分支最大为负还不如不选
            left = max(0, dfs(node.left))
            # 计算右边最大分支值，右边分支最大为负还不如不选
            right = max(0, dfs(node.right))
            # left-node-right为路径的值与已知最大值比较
            self.ans = max(self.ans, left + node.val + right)
            # 经过node单边的最大分支为当前node的父节点使用
            return max(left, right) + node.val

        dfs(root)
        return self.ans
# @lc code=end

