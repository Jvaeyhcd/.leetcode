#
# @lc app=leetcode.cn id=526 lang=python
#
# [526] 优美的排列
#

# @lc code=start
class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        vis = [False] * (n + 1)

        def backtrack(i, vis):
            if i > n:
                return 1
            
            ans = 0
            for num in range(1, n + 1):
                if not vis[num] and (i % num == 0 or num % i == 0):
                    vis[num] = True
                    ans += backtrack(i + 1, vis)
                    vis[num] = False
            return ans
        
        return backtrack(1, vis)

# @lc code=end

