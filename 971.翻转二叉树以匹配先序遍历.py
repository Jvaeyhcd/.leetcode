#
# @lc app=leetcode.cn id=971 lang=python3
#
# [971] 翻转二叉树以匹配先序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:

        ans = []
        i = 0

        def dfs(node: TreeNode):
            nonlocal i
            nonlocal ans
            if not node: return
            if node.val != voyage[i]:
                ans = [-1]
                return
            i += 1

            if i < len(voyage) and node.left and node.left.val != voyage[i]:
                ans.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        if ans and ans[0] == -1:
            ans = [-1]
        return ans
# @lc code=end

