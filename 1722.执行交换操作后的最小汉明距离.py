#
# @lc app=leetcode.cn id=1722 lang=python3
#
# [1722] 执行交换操作后的最小汉明距离
#

# @lc code=start

import collections
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.size -= 1

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

        
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        n = len(source)
        uf = UnionFind(n)
        for u, v in allowedSwaps:
            uf.union(u, v)
        
        ans = 0
        # 由于有重复的所以需要一个哈希表计数
        m = collections.defaultdict(lambda:collections.defaultdict(int))
        for i, num in enumerate(source):
            pa = uf.find(i)
            m[pa][num] += 1
        
        for i, num in enumerate(target):
            pa = uf.find(i)
            if m[pa][num] <= 0:
                ans += 1
            else:
                m[pa][num] -= 1

        return ans
# @lc code=end

solution = Solution()

source = [2,3,1]
target = [1,2,2]
allowedSwaps = [[0,2],[1,2]]

print(solution.minimumHammingDistance(source, target, allowedSwaps))