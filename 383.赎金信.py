#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnts = collections.defaultdict(lambda:0)
        for c in magazine:
            cnts[c] += 1
        for c in ransomNote:
            if cnts[c] > 0:
                cnts[c] -= 1
            else:
                return False
        return True
# @lc code=end

