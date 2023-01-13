#
# @lc app=leetcode.cn id=764 lang=python3
#
# [764] 最大加号标志
#

# @lc code=start
from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        zeros = set(tuple(a) for a in mines)
        for i in range(n):
            for j in range(n):
                if (i, j) in zeros:
                    print(i, j)
        return 0
# @lc code=end

