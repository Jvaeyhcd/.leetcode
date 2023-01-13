#
# @lc app=leetcode.cn id=2262 lang=python3
#
# [2262] 字符串的总引力
#

# @lc code=start
import collections


class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        indexs = collections.defaultdict(list)
        for i, ch in enumerate(s):
            indexs[ch].append(i)
        ans = 0
        for idxs in indexs.values():
            ans += n * (n + 1) // 2
            idxs = [-1] + idxs + [n]
            for pre, cur in zip(idxs, idxs[1:]):
                cnt = cur - pre
                ans -= cnt * (cnt - 1) // 2
        return ans
# @lc code=end

