#
# @lc app=leetcode.cn id=2006 lang=python3
#
# [2006] 差的绝对值为 K 的数对数目
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnts = Counter(nums)
        ans = 0
        for num, v in cnts.items():
            ans += cnts[num - k] * v
        return ans
# @lc code=end
S = Solution()
nums = [3,2,1,5,4]
k = 2
# nums= [1,3]
# k = 3
# nums = [1,2,2,1]
# k = 1
print(S.countKDifference(nums, k))
