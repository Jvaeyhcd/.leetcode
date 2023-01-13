#
# @lc app=leetcode.cn id=2306 lang=python3
#
# [2306] 公司命名
#

# @lc code=start
import collections
from itertools import combinations
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = [set() for _ in range(26)]
        for w in ideas:
            groups[ord(w[0]) - ord("a")].add(w[1:])
        ans = 0
        for a, b in combinations(groups, 2):
            m = len(a & b)
            ans += (len(a) - m) * (len(b) - m)
        return ans * 2


    # def distinctNames(self, ideas: List[str]) -> int:
    #     groups = collections.defaultdict(int)
    #     for word in ideas:
    #         groups[word[1:]] |= 1 << (ord(word[0]) - ord("a"))
        
    #     ans = 0
    #     cnt = [[0] * 26 for _ in range(26)]
    #     for mask in groups.values():
    #         for i in range(26):
    #             if mask & (1 << i) == 0:
    #                 for j in range(26):
    #                     if mask & (1 << j):
    #                         cnt[i][j] += 1
    #             else:
    #                 for j in range(26):
    #                     if mask & (1 << j) == 0:
    #                         ans += cnt[i][j]
    #     return ans * 2
# @lc code=end

