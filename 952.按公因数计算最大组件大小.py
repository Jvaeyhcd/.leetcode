#
# @lc app=leetcode.cn id=952 lang=python3
#
# [952] 按公因数计算最大组件大小
#

# @lc code=start
import collections
import math
from typing import List


class UnionFind:
    def __init__(self):
        self.parent = collections.defaultdict(lambda:0)
        self.size = 0


    def add(self, x: int):
        self.parent[x] = x
        self.size += 1

    
    def find(self, x: int):
        if x not in self.parent:
            self.add(x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    

    def merge(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.size -= 1


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        uf = UnionFind()
        for i, num in enumerate(nums):
            c = num
            for k in range(2, int(math.sqrt(num) + 1)):
                flag = False
                while num % k == 0:
                    num = num // k
                    flag = True
                if flag:
                    uf.merge(c, k)
            if num > 1:
                uf.merge(c, num)
        ans = 1
        cnts = collections.defaultdict(lambda:0)
        for num in nums:
            root_num = uf.find(num)
            cnts[root_num] += 1
            ans = max(ans, cnts[root_num])
        return ans
# @lc code=end

s = Solution()
nums = [4,6,15,35]
nums = [20,50,9,63]
nums = [2,3,6,7,4,12,21,39]
print(s.largestComponentSize(nums))