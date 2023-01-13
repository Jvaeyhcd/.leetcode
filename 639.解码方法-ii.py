#
# @lc app=leetcode.cn id=639 lang=python3
#
# [639] 解码方法 II
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        MOD = 10**9+7
        dp = [0 for _ in range(n + 1)]

        def check1(ch: str) -> int:
            if ch == '0':
                return 0
            return 9 if ch == '*' else 1
        
        def check2(ch1: str, ch2: str) -> int:
            if ch1 == ch2 == '*':
                return 15
            if ch1 == '*':
                return 2 if ch2 <= '6' else 1
            if ch2 == '*':
                return 9 if ch1 == '1' else (6 if ch1 == '2' else 0)
            return int(ch1 != '0' and int(ch1) * 10 + int(ch2) <= 26)
        dp[0] = 1
        for i in range(1, n + 1):
            if i == 1:
                dp[i] = check1(s[i - 1])
                if dp[i] == 0:
                    return 0
            else:
                c = dp[i - 1] * check1(s[i - 1])
                if i > 1:
                    c += dp[i - 2] * check2(s[i - 2], s[i - 1])
                c %= MOD
                dp[i] = c

        return dp[n]

# @lc code=end
S = Solution()
s = "*1*1*0"
s = "*********"
print(S.numDecodings(s))
