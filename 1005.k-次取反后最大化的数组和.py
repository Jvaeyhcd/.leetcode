#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

# @lc code=start
from typing import List
import collections


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        number = collections.defaultdict(lambda:0)
        for num in nums:
            number[100 + num] += 1
        i = 0
        while k > 0:
            while number[i] == 0:
                i += 1
            number[i] -= 1
            number[200 - i] += 1
            if i > 100:
                i = 200 - i
            k -= 1
        ans = 0
        for j in range(i, 201):
            ans += (j - 100) * number[j]
        return ans

# @lc code=end

