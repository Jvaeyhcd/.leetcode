#
# @lc app=leetcode.cn id=2063 lang=python3
#
# [2063] 所有子字符串中的元音
#

# @lc code=start
class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0
        n = len(word)
        for i, ch in enumerate(word):
            if ch in 'aeiou':
                ans += (i + 1) * (n - i)
        return ans

# @lc code=end
# 动态规划
import collections

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        # dp[i]表示以word下标为i结尾的子串包含元音字符的个数
        dp = [0 for _ in range(n)]
        ans = 0
        if word[0] in 'aeiou':
            dp[0] = 1
            ans = 1
        for i in range(1, n):
            if word[i] in 'aeiou':
                dp[i] = dp[i - 1] + (i + 1)
            else:
                dp[i] = dp[i - 1]
            ans += dp[i]
        return ans
