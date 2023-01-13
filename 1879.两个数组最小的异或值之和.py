#
# @lc app=leetcode.cn id=1879 lang=python3
#
# [1879] 两个数组最小的异或值之和
#

# @lc code=start
import functools
from typing import List


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        @functools.lru_cache(None)
        def dfs(i: int, mask: int) -> int:
            if i == n:
                return 0
            res = 0xf3f3f3f3
            for j in range(n):
                if mask & (1 << j) == 0:
                    res = min(res, (nums1[i] ^ nums2[j]) + dfs(i + 1, mask | (1 << j)))
            return res
        
        return dfs(0, 0)
# @lc code=end

S = Solution()
nums1 = [72,97,8,32,15]
nums2 = [63,97,57,60,83]

print(S.minimumXORSum(nums1, nums2))
