#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc code=start
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexs = []
        for i, ch in enumerate(s):
            if ch == c:
                indexs.append(i)
        n = len(s)
        ans = [0 for _ in range(n)]
        for i, ch in enumerate(s):
            if ch != c:
                left = bisect_left(indexs, i)
                if 0 <= left < len(indexs):
                    ans[i] = abs(indexs[left] - i) if ans[i] == 0 else min(ans[i], indexs[left] - i)
                if left - 1 >= 0:
                    ans[i] = abs(indexs[left - 1] - i) if ans[i] == 0 else min(ans[i], abs(indexs[left - 1] - i))
                if left + 1 < len(indexs):
                    ans[i] = abs(indexs[left + 1] - i) if ans[i] == 0 else min(ans[i], abs(indexs[left + 1] - i))
                
        return ans
        
# @lc code=end
s = "aaba"
c = "b"
solution = Solution()
print(solution.shortestToChar(s, c))
