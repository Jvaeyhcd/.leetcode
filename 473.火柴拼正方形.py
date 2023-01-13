#
# @lc app=leetcode.cn id=473 lang=python3
#
# [473] 火柴拼正方形
#

# @lc code=start
from functools import lru_cache
from typing import List

# 回溯算法
# class Solution:
#     def makesquare(self, matchsticks: List[int]) -> bool:
#         total = sum(matchsticks)
#         if total % 4 != 0:
#             return False
        
#         width = total // 4
#         # 四条边的长度
#         widths = [0 for _ in range(4)]
#         n = len(matchsticks)
#         matchsticks.sort(reverse=True)
#         def backtrack(index: int) -> bool:
#             if index == n:
#                 return widths[0] == widths[1] == widths[2] == width
#             for i in range(4):
#                 if widths[i] + matchsticks[index] <= width:
#                     widths[i] += matchsticks[index]
#                     if backtrack(index + 1):
#                         return True
#                     widths[i] -= matchsticks[index]
#             return False
        
#         return backtrack(0)

# 状态压缩动态规划（记忆化搜索）
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks: 
            return False
        n = len(matchsticks)
        total = sum(matchsticks)
        width = total // 4
        if width * 4 != total:
            return False

        @lru_cache(None)
        def recurse(mask: int, side_done: int) -> bool:
            total = 0
            for i in range(n):
                if mask & (1 << i):
                    total += matchsticks[i]
            
            if total > 0 and total % width == 0:
                side_done += 1
            
            if side_done == 3:
                return True

            left = ((total // width) + 1) * width - total

            ans = False
            for i in range(n):
                if matchsticks[i] <= left and mask & (1 << i) == 0:
                    if recurse(mask ^ (1 << i), side_done):
                        ans = True
                        break

            return ans
        
        return recurse(0, 0)

# @lc code=end

S = Solution()
matchsticks = [1,1,2,2,2]
# matchsticks = [3,3,3,3,4]
matchsticks = [3,3,3,3,4,4,4,4]
matchsticks = [5,5,5,5,4,4,4,4,3,3,3,3]

print(S.makesquare(matchsticks))
# print(5*4*3*2*1)