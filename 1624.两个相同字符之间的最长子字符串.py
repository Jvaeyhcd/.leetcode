#
# @lc app=leetcode.cn id=1624 lang=python3
#
# [1624] 两个相同字符之间的最长子字符串
#

# @lc code=start
import collections


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indexs = collections.defaultdict(list)
        ans = -1
        for i, c in enumerate(s):
            indexs[c].append(i)
            if len(indexs[c]) > 1:
                ans = max(indexs[c][-1] - indexs[c][0] - 1, ans)
        return ans
# @lc code=end

solution = Solution()
s = "mgntdygtxrvxjnwksqhxuxtrv"
print(solution.maxLengthBetweenEqualCharacters(s))