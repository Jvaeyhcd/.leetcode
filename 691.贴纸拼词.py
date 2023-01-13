#
# @lc app=leetcode.cn id=691 lang=python3
#
# [691] 贴纸拼词
#

# @lc code=start
from typing import Counter, List

# 背包DP+状态压缩
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m, n = len(stickers), len(target)
        INF = 0xf3f3f3f3
        dp = [INF for _ in range(1 << n)]
        dp[0] = 0
        for sticker in stickers:
            for status in range(1 << n):
                if dp[status] == INF:
                    continue
                cur_status = status
                for c in sticker:
                    for i in range(n):
                        if c == target[i] and (cur_status & (1 << i)) == 0:
                            cur_status |= (1 << i)
                            break
                dp[cur_status] = min(dp[cur_status], dp[status] + 1)
        return dp[(1 << n) - 1] if dp[(1 << n) - 1] != INF else -1
# @lc code=end
S = Solution()
stickers = ["with","example","science"]
target = "thehat"
print(S.minStickers(stickers, target))
