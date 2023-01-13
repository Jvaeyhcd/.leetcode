#
# @lc app=leetcode.cn id=1161 lang=python3
#
# [1161] 最大层内元素和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        arr = []
        q = collections.deque([root])
        ans, max_s, level = 0, -0xf3f3f3, 1
        while q:
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if s > max_s:
                max_s = s
                ans = level
            level += 1
        return ans
        
# @lc code=end

