#
# @lc app=leetcode.cn id=1998 lang=python3
#
# [1998] 数组的最大公因数排序
#

# @lc code=start
import collections
import math
from typing import List


class UnionFind:
    def __init__(self):
        self.parents = collections.defaultdict(int)

    
    def add(self, x: int):
        self.parents[x] = x
    

    def find(self, x: int):
        if x not in self.parents:
            self.add(x)
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parents[root_x] = root_y


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        nums1 = sorted(nums)
        uf = UnionFind()
        for num in nums:
            c = num
            for i in range(2, int(math.sqrt(num)) + 1):
                flag = False
                while num % i == 0:
                    num = num // i
                    flag = True
                if flag:
                    uf.union(c, i)
            if num > 1:
                uf.union(c, num)
        
        for i in range(len(nums)):
            if uf.find(nums[i]) != uf.find(nums1[i]):
                return False
        return True

# @lc code=end

s = Solution()
nums = [5,2,6,2]
nums = [10,5,9,3,15]
nums = [8,4,15,2,9,21]
print(s.gcdSort(nums))