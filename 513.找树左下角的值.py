#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Optional


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = None
        queue = collections.deque()
        queue.append(root)
        while queue:
            ans = queue[0]
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return ans.val


# @lc code=end

