#
# @lc app=leetcode.cn id=828 lang=python3
#
# [828] 统计子串中的唯一字符
#

# @lc code=start
import collections


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        MOD = 10**9 + 7
        ns = len(s)
        mp = collections.defaultdict(lambda:[])
        for i, ch in enumerate(s):
            mp[ch].append(i)
        
        ans = 0
        for indexs in mp.values():
            n = len(indexs)
            for i in range(n):
                start = indexs[i - 1] if i > 0 else -1
                end = indexs[i + 1] if i < n - 1 else ns
                ans += (indexs[i] - start) * (end - indexs[i])
        return ans % MOD
        
# @lc code=end

