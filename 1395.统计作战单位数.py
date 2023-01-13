#
# @lc app=leetcode.cn id=1395 lang=python3
#
# [1395] 统计作战单位数
#

# @lc code=start
import collections
from typing import List


class FenwickTree:
    def __init__(self, n: int):
        self.bit_arr = [0] * (n + 1)

    def lowbit(self, x: int):
        return x & (-x)

    def update(self, idx: int, delta: int):
        n = len(self.bit_arr)
        while idx < n:
            self.bit_arr[idx] += delta
            idx += self.lowbit(idx)
    
    def query(self, idx: int):
        ans = 0
        while idx:
            ans += self.bit_arr[idx]
            idx -= self.lowbit(idx)
        return ans


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        bit = FenwickTree(n)
        h = [i for i in range(n)]
        h.sort(key=lambda x:rating[x])
        mp = collections.defaultdict(int)
        for i in range(n):
            mp[rating[h[i]]] = i + 1
        ans = 0
        for i in range(n):
            index = mp[rating[i]]
            # 前面比他小的个数
            a = bit.query(index)
            # 前面比他大的个数
            b = i - a
            # 后面比他小的个数
            c = index - 1 - a
            # 后面比他大的个数
            d = n - 1 - a - b - c
            ans += (a * d + b * c)
            bit.update(index, 1)
        return ans
# @lc code=end

solution = Solution()
rating = [2,5,3,4,1]
print(solution.numTeams(rating))