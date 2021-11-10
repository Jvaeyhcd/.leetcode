#
# @lc app=leetcode.cn id=1305 lang=python3
#
# [1305] 两棵二叉搜索树中的所有元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 中序遍历+归并排序
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def dfs(root: TreeNode):
            if not root: return []
            return dfs(root.left) + [root.val] + dfs(root.right)
        
        v1 = dfs(root1)
        v2 = dfs(root2)

        ans = []
        i, j = 0, 0
        while i < len(v1) or j < len(v2):
            if i < len(v1) and (j == len(v2) or v1[i] <= v2[j]):
                ans.append(v1[i])
                i += 1
            else:
                ans.append(v2[j])
                j += 1
        return ans

# @lc code=end

# 常规解法，遍历后再排序
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def dfs(root: TreeNode):
            if not root: return []
            return dfs(root.left) + [root.val] + dfs(root.right)
        
        return sorted(dfs(root1) + dfs(root2))