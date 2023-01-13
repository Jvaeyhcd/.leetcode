#
# @lc app=leetcode.cn id=1755 lang=python3
#
# [1755] 最接近目标值的子序列和
#

# @lc code=start
from typing import List
import bisect

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        m = n // 2
        arr1 = []
        for i in range(1 << m):
            tot = 0
            for j, x in enumerate(nums[:m]):
                if i >> j & 1:
                    tot += x
            if tot == goal:
                return 0
            arr1.append(tot)
        
        arr2 = []
        for i in range(1 << (n - m)):
            tot = 0
            for j, x in enumerate(nums[m:]):
                if i >> j & 1:
                    tot += x
            arr2.append(tot)
        
        ans = 10 ** 10
        arr1.sort()
        for tot in arr2:
            idx = bisect.bisect_right(arr1, goal - tot)
            if idx == len(arr1):
                idx = len(arr1) - 1
            if idx - 1 >= 0:
                if abs(goal - arr1[idx - 1] - tot) < abs(goal - arr1[idx] - tot):
                    idx = idx - 1
            if abs(arr1[idx] + tot - goal) < ans:
                ans = abs(arr1[idx] + tot - goal)
            
        return ans
# @lc code=end

