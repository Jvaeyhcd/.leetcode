#
# @lc app=leetcode.cn id=798 lang=python3
#
# [798] 得分最高的最小轮调
#

# @lc code=start
from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diffs = [0 for _ in range(n)]
        for i, num in enumerate(nums):
            low = (i + 1) % n
            high = (i - num + n + 1) % n
            diffs[low] += 1
            diffs[high] -= 1
            if low >= high:
                diffs[0] += 1
            
        score, maxS, ans = 0, 0, 0
        for i in range(n):
            score += diffs[i]
            if score > maxS:
                maxS = score
                ans = i
        return ans

# @lc code=end
solution = Solution()
nums = [2,3,1,4,0]
print(solution.bestRotation(nums))