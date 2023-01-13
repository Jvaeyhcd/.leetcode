#
# @lc app=leetcode.cn id=1312 lang=python3
#
# [1312] 让字符串成为回文串的最少插入次数
#

# @lc code=start
from typing import Counter


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        l, r = 0, n - 1
        cnt_left = Counter()
        cnt_right = Counter()
        while l < r:
            cnt_left[s[l]] += 1
            cnt_right[s[r]] += 1
            l += 1
            r -= 1
        ans = 0
        for i in range(26):
            ch = chr(ord('a') + i)
            ans += abs(cnt_left[ch] - cnt_right[ch])
        if l != r and ans > 0:
            ans -= 1
        return ans

# @lc code=end

solution = Solution()
s = "mbadm"
s = "leetcodee"
print(solution.minInsertions(s))