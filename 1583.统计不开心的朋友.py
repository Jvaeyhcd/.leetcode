#
# @lc app=leetcode.cn id=1583 lang=python
#
# [1583] 统计不开心的朋友
#

# @lc code=start
class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        order = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                order[i][preferences[i][j]] = j
        
        match = [0] * n
        for x, y in pairs:
            match[x] = y
            match[y] = x
        
        ans = 0
        for x in range(n):
            y = match[x]
            index = order[x][y]
            for i in range(index):
                u = preferences[x][i]
                v = match[u]
                if order[u][x] < order[u][v]:
                    ans += 1
                    break
        return ans

# @lc code=end

