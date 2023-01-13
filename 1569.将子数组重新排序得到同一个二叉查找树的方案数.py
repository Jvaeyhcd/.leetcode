#
# @lc app=leetcode.cn id=1569 lang=python3
#
# [1569] 将子数组重新排序得到同一个二叉查找树的方案数
#

# @lc code=start
from math import comb
from typing import List


class TreeNode:
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val
        self.size = 1
        self.ans = 0


class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        MOD = 1_000_000_007
        n = len(nums)
        if n == 1:
            return 0
        root = TreeNode(nums[0])

        def insert(val: int):
            cur = root
            while True:
                cur.size += 1
                if val < cur.val:
                    if not cur.left:
                        cur.left = TreeNode(val)
                        return
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = TreeNode(val)
                        return
                    cur = cur.right
            
        def dfs(node: TreeNode):
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)

            lsize = node.left.size if node.left else 0
            rsize = node.right.size if node.right else 0
            lans = node.left.ans if node.left else 1
            rans = node.right.ans if node.right else 1

            node.ans = comb(lsize + rsize, lsize) * lans * rans % MOD

        for num in nums[1:]:
            insert(num)
        
        dfs(root)
        return (root.ans - 1 + MOD) % MOD

# @lc code=end

