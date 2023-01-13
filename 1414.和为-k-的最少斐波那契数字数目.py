#
# @lc app=leetcode.cn id=1414 lang=python3
#
# [1414] 和为 K 的最少斐波那契数字数目
#

# @lc code=start
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        MAX = 10**9+1
        dp = [1, 1]
        i = 2
        while dp[i - 1] + dp[i - 2] < MAX:
            dp.append(dp[i - 1] + dp[i - 2])
            i += 1
        ans = 0
        while k > 0:
            idx = 0
            for i in range(len(dp)):
                if dp[i] <= k:
                    idx = i
                else:
                    break
            k -= dp[idx]
            ans += 1
        return ans
                    

        
# @lc code=end

