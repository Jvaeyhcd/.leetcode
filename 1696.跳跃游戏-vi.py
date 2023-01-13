#
# @lc app=leetcode.cn id=1696 lang=python3
#
# [1696] 跳跃游戏 VI
#

# @lc code=start
from queue import PriorityQueue
from typing import List

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans, q = nums[0], PriorityQueue()
        q.put([-nums[0], 0])
        for i in range(1, len(nums)):
            while not q.empty():
                top = q.get()
                if i - top[-1] <= k:
                    q.put(top)
                    break
            ans = -top[0] + nums[i]
            q.put([-ans, i])
        return ans
            



# 超时算法，记忆化搜索
# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         @functools.lru_cache(None)
#         def dfs(i: int) -> int:
#             if i == n - 1:
#                 return nums[i]
#             ans = nums[i]
#             ans += max(dfs(i + l) for l in range(1, k + 1) if i + l < n)
#             return ans
#         return dfs(0)
# @lc code=end
nums = [1,-1,-2,4,-7,3]
k = 2
nums = [10,-5,-2,4,0,3]
k = 3
# nums = [1,-5,-20,4,-1,3,-6,-3]
# k = 2
s = Solution()
print(s.maxResult(nums, k))