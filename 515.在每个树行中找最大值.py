#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            res = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                res = max(res, node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(res)
        return ans
# @lc code=end

