#
# @lc app=leetcode.cn id=1409 lang=python3
#
# [1409] 查询带键的排列
#

# @lc code=start
from typing import List

class FenwickTree:
    def __init__(self, n: int):
        self.bit_arr = [0 for _ in range(n + 1)]
    
    def lowbit(self, x: int) -> int:
        return x & (-x)

    def update(self, idx: int, delta: int):
        n = len(self.bit_arr)
        while idx < n:
            self.bit_arr[idx] += delta
            idx += self.lowbit(idx)
    
    def query(self, idx: int) -> int:
        ans = 0
        while idx:
            ans += self.bit_arr[idx]
            idx -= self.lowbit(idx)
        return ans


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        n = len(queries)
        BIT = FenwickTree(m + n)

        pos = [0] * (m + 1)
        for i in range(1, m + 1):
            pos[i] = n + i
            BIT.update(n + i, 1)
        
        ans = []
        for i, q in enumerate(queries):
            cur = pos[q]
            BIT.update(cur, -1)
            ans.append(BIT.query(cur))
            cur = pos[q] = n - i
            BIT.update(cur, 1)
        return ans

# @lc code=end
queries = [4,1,2,2]
m = 4
solution = Solution()
print(solution.processQueries(queries, m))
