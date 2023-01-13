#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(root: TreeNode) -> List[int]:
            if not root:
                return []
            left = inorder(root.left)
            right = inorder(root.right)
            return left + [root.val] + right
        
        arr = inorder(root)
        mp = collections.defaultdict(int)
        for i, num in enumerate(arr):
            if k - num in mp:
                return True
            mp[num] = i
        return False
# @lc code=end

