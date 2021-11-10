#
# @lc app=leetcode.cn id=839 lang=python
#
# [839] 相似字符串组
#

# @lc code=start
class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        UFS = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if self.check(strs[i], strs[j]):
                    UFS.union(i, j)
        
        return UFS.size

    def check(self, str1, str2):
        # 字符不同的次数
        cnt = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                cnt += 1
            if cnt > 2:
                return False
        
        return True

class UnionFind(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        # 代表连通分量
        self.size = n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.size -= 1
# @lc code=end

