#
# @lc app=leetcode.cn id=2000 lang=python3
#
# [2000] 反转单词前缀
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = -1
        for i, c in enumerate(word):
            if c == ch:
                idx = i
                break
        if idx > 0:
            return word[:idx+1][::-1] + word[idx+1:]
        return word
# @lc code=end

