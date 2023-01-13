#
# @lc app=leetcode.cn id=2167 lang=python3
#
# [2167] 移除所有载有违禁货物车厢所需的最少时间
#

# @lc code=start
class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        suf = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                suf[i] = suf[i + 1]
            else:
                suf[i] = min(suf[i + 1] + 2, n - i)
        
        ans = suf[0]
        pre = 0
        for i, ch in enumerate(s):
            if ch == '1':
                pre = min(pre + 2, i + 1)
                ans = min(ans, pre + suf[i + 1])
        return ans
# @lc code=end

