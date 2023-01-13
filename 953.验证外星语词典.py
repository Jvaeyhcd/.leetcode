#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        indexs = {c: i for i, c in enumerate(order)}
        n = len(words)
        for i in range(n - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if indexs[word1[j]] > indexs[word2[j]]:
                    return False
                elif indexs[word1[j]] < indexs[word2[j]]:
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True
# @lc code=end

