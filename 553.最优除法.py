#
# @lc app=leetcode.cn id=553 lang=python3
#
# [553] 最优除法
#

# @lc code=start
from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        self.min_val = -float('inf')
        def dfs(path: List[int]):
            
# @lc code=end

