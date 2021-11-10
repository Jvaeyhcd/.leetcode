#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def generate(start: int, end: int) -> List[TreeNode]:
            if start > end: return [None]
            ans = []
            for i in range(start, end + 1):
                leftTrees = generate(start, i - 1)
                rightTrees = generate(i + 1, end)
                for left in leftTrees:
                    for right in rightTrees:
                        node = TreeNode(i)
                        node.left = left
                        node.right = right
                        ans.append(node)
            return ans
        
        return generate(1, n)

# @lc code=end

