#
# @lc app=leetcode.cn id=1996 lang=python3
#
# [1996] 游戏中弱角色的数量
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        max_def = 0
        for _, defense in properties:
            if max_def > defense:
                ans += 1
            else:
                max_def = defense
        return ans
        

# @lc code=end

s = Solution()
properties = [[5,5],[6,3],[3,6]]
properties = [[2,2],[3,3]]
# properties = [[1,5],[10,4],[4,3]]
print(s.numberOfWeakCharacters(properties))