#
# @lc app=leetcode.cn id=765 lang=python
#
# [765] 情侣牵手
#

# @lc code=start
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)
        m = n // 2
        UFS = UnionFind(m)
        for i in range(m):
            UFS.add(i)
        
        for i in range(m):
            UFS.union(row[2 * i] / 2, row[2 * i + 1] / 2)
        
        cnt = 0
        for i in range(m):
            if i == UFS.find(i):
                cnt += 1
        
        return m - cnt

class UnionFind(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def add(self, x):
        self.parent[x] = x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
# @lc code=end

