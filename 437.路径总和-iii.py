#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        
        def dfs(root: TreeNode, target: int) -> int:
            if not root: return 0
            ans = 0
            if root.val == target: ans += 1
            ans += dfs(root.left, target - root.val)
            ans += dfs(root.right, target - root.val)
            return ans
        
        if not root: return 0
        ans = dfs(root, targetSum)
        ans += self.pathSum(root.left, targetSum)
        ans += self.pathSum(root.right, targetSum)
        return ans


# @lc code=end

# 前缀和+dfs
class Solution:
    def __init__(self):
        # prefix记录前缀和为某个值的次数
        self.prefix = collections.defaultdict(lambda:0)

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.prefix[0] = 1
        return self.dfs(root, 0, targetSum)

    def dfs(self, root: TreeNode, cur: int, target: int) -> int:
        if not root: return 0
        ans = 0
        cur += root.val
        if cur - target in self.prefix:
            ans = self.prefix[cur - target]
        self.prefix[cur] += 1
        ans += self.dfs(root.left, cur, target)
        ans += self.dfs(root.right, cur, target)
        self.prefix[cur] -= 1
        return ans