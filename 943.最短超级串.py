#
# @lc app=leetcode.cn id=943 lang=python3
#
# [943] 最短超级串
#

# @lc code=start
import functools
from typing import List


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)

        # mask为单词的选中状态
        def dfs(mask: int):
            word = 


# @lc code=end

