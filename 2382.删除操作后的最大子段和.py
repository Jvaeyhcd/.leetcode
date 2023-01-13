#
# @lc app=leetcode.cn id=2382 lang=python3
#
# [2382] 删除操作后的最大子段和
#

# @lc code=start
from typing import List

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        vis = set()

        self.parent = [i for i in range(n)]
        self.values = [nums[i] for i in range(n)]

        def find(x: int) -> int:
            if self.parent[x] != x:
                self.parent[x] = find(self.parent[x])
            return self.parent[x]

        def union(x: int, y: int) -> int:
            rx, ry = find(x), find(y)
            if rx != ry:
                if rx < ry:
                    rx, ry = ry, rx
                self.parent[rx] = ry
                self.values[ry] += self.values[rx]
                return self.values[ry]
            return self.values[rx]

        
        mx = 0
        ans = []
        for i in removeQueries[::-1]:
            ans.append(mx)
            mx = max(mx, self.values[i])
            if i - 1 >= 0 and i - 1 in vis:
                mx = max(mx, union(i - 1, i))
            if i + 1 < n and i + 1 in vis:
                mx = max(mx, union(i + 1, i))
            vis.add(i)
        return ans[::-1]

# @lc code=end

