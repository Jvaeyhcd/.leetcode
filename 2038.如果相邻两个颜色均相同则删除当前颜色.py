#
# @lc app=leetcode.cn id=2038 lang=python3
#
# [2038] 如果相邻两个颜色均相同则删除当前颜色
#

# @lc code=start
import collections


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        freq = collections.defaultdict(lambda:0)
        cur, cnt = '', 0
        for c in colors:
            if cur != c:
                cur = c
                cnt = 1
            else:
                cnt += 1
                if cnt >= 3:
                    freq[cur] += 1
        return freq['A'] > freq['B']
# @lc code=end

