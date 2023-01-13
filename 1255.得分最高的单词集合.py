#
# @lc app=leetcode.cn id=1255 lang=python3
#
# [1255] 得分最高的单词集合
#

# @lc code=start
from typing import Counter, List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        cnts1 = Counter(letters)
        n = len(words)
        mp = {chr(ord('a') + i): s for i, s in enumerate(score)}
        ans = 0
        for mask in range(1 << n):
            cnts2 = Counter()
            total = 0
            for i, word in enumerate(words):
                if mask & (1 << i):
                    for ch in word:
                        cnts2[ch] += 1
                        total += mp[ch]
            
            flag = True
            for i in range(26):
                ch = chr(ord('a') + i)
                if cnts2[ch] > cnts1[ch]:
                    flag = False
                    break
            if flag:
                ans = max(ans, total)
        return ans
# @lc code=end

