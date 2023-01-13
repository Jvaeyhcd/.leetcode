#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start
import functools
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums: return False
        sums = sum(nums)
        width = sums // k
        if width * k != sums:
            return False
        n = len(nums)
        
        @functools.lru_cache(None)
        def dfs(mask: int, side_done) -> bool:
            # mask二进制011011，1代表没有被选，0代表已经被选
            total = 0
            for i in range(n - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += nums[n - 1 - i]
            
            if total > 0 and total % width == 0:
                side_done += 1
            
            if side_done == k - 1:
                return True
            
            c = int(total / width)
            # 剩下的部分可以通过多少来填满
            rem = width * (c + 1) - total

            for i in range(n - 1, -1, -1):
                if nums[n - 1 - i] <= rem and mask & (1 << i):
                    if dfs(mask ^ (1 << i), side_done):
                        return True
            return False

        return dfs((1 << n) - 1, 0)
# @lc code=end
S = Solution()
nums = [4, 3, 2, 3, 5, 2, 1]
k = 3
print(S.canPartitionKSubsets(nums, k))