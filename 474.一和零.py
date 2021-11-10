#
# @lc app=leetcode.cn id=474 lang=python
#
# [474] 一和零
#

# @lc code=start
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        l = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(l + 1)]
        for i in range(1, l + 1):
            arr = self.get_zeros_ones(strs[i - 1])
            for j in range(m + 1):
                for k in range(n + 1):
                    if j < arr[0] or k < arr[1]:
                        dp[i][j][k] = dp[i - 1][j][k]
                    elif j >= arr[0] and k >= arr[1]:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - arr[0]][k - arr[1]] + 1)

        return dp[l][m][n]

    def get_zeros_ones(self, str):
        ans = [0, 0]
        for s in str:
            if s == '0':
                ans[0] += 1
            elif s == '1':
                ans[1] += 1
        
        return ans
# @lc code=end

