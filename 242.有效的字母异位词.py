#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnts1 = collections.defaultdict(lambda:0)
        cnts2 = collections.defaultdict(lambda:0)
        for c in s:
            cnts1[c] += 1
        for c in t:
            cnts2[c] += 1
        
        if len(cnts1.keys()) != len(cnts2.keys()): return False
        
        for k in cnts1.keys():
            if cnts1[k] != cnts2[k]: return False
        
        return True

# @lc code=end

