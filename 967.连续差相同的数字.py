#
# @lc app=leetcode.cn id=967 lang=python3
#
# [967] 连续差相同的数字
#

# @lc code=start
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        def backtack(path: List[int], level: int):
            if level == n:
                num = 0
                for a in path:
                    num  = num * 10 + a
                ans.append(num)
                return
            
            for num in range(10):
                if abs(path[-1] - num) == k:
                    backtack(path + [num], level + 1)
        
        for i in range(1, 10):
            backtack([i], 1)
        return ans
# @lc code=end

S = Solution()
n = 2
k = 1
n = 2
k = 0
print(S.numsSameConsecDiff(n, k))