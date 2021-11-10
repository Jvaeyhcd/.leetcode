#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        ans = []
        # 回溯
        def backtrack(cur: TreeNode, path: List[int], target: int, ans: List[int]):
            if not cur.left and not cur.right:
                # 叶子节点
                if target == 0:
                    ans.append(path + [])
                return
            
            if cur.left: backtrack(cur.left, path + [cur.left.val], target - cur.left.val, ans)
            if cur.right: backtrack(cur.right, path + [cur.right.val], target - cur.right.val, ans)
        
        backtrack(root, [root.val], targetSum - root.val, ans)
        return ans
        
# @lc code=end

