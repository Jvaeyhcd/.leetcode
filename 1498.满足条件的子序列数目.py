#
# @lc app=leetcode.cn id=1498 lang=python3
#
# [1498] 满足条件的子序列数目
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9+7
        n = len(nums)
        f = [0] * n
        f[0] = 1
        for i in range(1, n):
            f[i] = (f[i - 1] * 2) % MOD
        
        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            if num * 2 > target:
                break
            max_value = target - num
            pos = bisect.bisect_right(nums, max_value) - 1
            contribute = f[pos - i] if pos >= i else 0
            ans += contribute
        return ans % MOD
        
# @lc code=end

solution = Solution()
nums = [14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14]
target = 22
print(solution.numSubseq(nums, target))