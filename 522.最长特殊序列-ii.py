#
# @lc app=leetcode.cn id=522 lang=python3
#
# [522] 最长特殊序列 II
#

# @lc code=start
from typing import Counter, List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        ans = -1
        for i, s in enumerate(strs):
            if len(s) > ans:
                if all(not self.isSubStr(s, ss) for j, ss in enumerate(strs) if i != j):
                    ans = len(s)
        return ans

    def isSubStr(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        i = j = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s1)


# @lc code=end

solution = Solution()
strs = ["aba","cdc","eae"]
print(solution.findLUSlength(strs))