#
# @lc app=leetcode.cn id=805 lang=python3
#
# [805] 数组的均值分割
#

# @lc code=start
import collections
import datetime
from functools import lru_cache
from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n == 1: return False
        s = sum(nums)
        for i in range(n):
            nums[i] = nums[i] * n - s
        
        m = n // 2
        left = set()
        for i in range(1, 1 << m):
            tot = 0
            for j, x in enumerate(nums[:m]):
                if i >> j & 1:
                    tot += x
            if tot == 0:
                return True
            left.add(tot)
        
        rsum = sum(nums[m:])
        for i in range(1, 1 << (n - m)):
            tot = 0
            for j, x in enumerate(nums[m:]):
                if i >> j & 1:
                    tot += x
            if tot == 0 or (rsum != tot and -tot in left):
                return True
        return False

        

# @lc code=end
solution = Solution()
# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31]
# nums = [2,2,2,2,2,2]
# nums = [3,1]
# nums = [1,1,1,1,4,6,9,9,9,9]
# nums = [60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]
# nums = [60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]
# nums = [1,6,2,3]
# nums = [5,3,11,19,2]
# nums = [2,3,5,11,19]
# nums = [19,11,5,3,2]
# nums = [18,0,16,2]
# nums = [18,16,2,0]
# nums = [0,2,16,18]
nums = [33,86,88,78,21,76,19,20,88,76,10,25,37,97,58,89,65,59,98,57,50,30,58,5,61,72,23,6]
starttime = datetime.datetime.now()
print(solution.splitArraySameAverage(nums))
endtime = datetime.datetime.now()
# print((endtime - starttime))