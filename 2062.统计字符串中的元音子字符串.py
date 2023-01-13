#
# @lc app=leetcode.cn id=2062 lang=python3
#
# [2062] 统计字符串中的元音子字符串
#

# @lc code=start
# 滑动窗口
import collections

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        ans, l = 0, 0
        for r in range(n):
            if word[r] not in 'aeiou':
                l = r + 1
                continue
            if r == n - 1 or word[r + 1] not in 'aeiou':
                cnts = collections.defaultdict(lambda:0)
                left = l
                for i in range(l, r + 1):
                    cnts[word[i]] += 1
                    while cnts[word[left]] > 1:
                        cnts[word[left]] -= 1
                        left += 1
                    if len(cnts) == 5:
                        ans += (left - l + 1)
        return ans
# @lc code=end

