#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        n = len(root.children)
        for i in range(n):
            ans += self.postorder(root.children[i])
        ans += [root.val]
        return ans
        
        
# @lc code=end

