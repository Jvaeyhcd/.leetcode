#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 中序遍历
        self.arr = []
        def inorder(root: TreeNode):
            if not root: return
            inorder(root.left)
            self.arr.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return self.arr[k - 1]
# @lc code=end

