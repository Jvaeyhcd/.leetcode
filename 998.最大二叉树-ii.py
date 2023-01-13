#
# @lc app=leetcode.cn id=998 lang=python3
#
# [998] 最大二叉树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        prev, cur = None, root
        node = TreeNode(val)

        while cur and cur.val > val:
            prev = cur
            cur = cur.next
        
        if not prev:
            node.left = cur
            return node
        else:
            prev.right = node
            node.left = cur
            return root
# @lc code=end

