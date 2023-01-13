#
# @lc app=leetcode.cn id=1636 lang=python3
#
# [1636] 按照频率将数组升序排序
#

# @lc code=start
from typing import Counter, List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        nums.sort(key=lambda x: (counter[x], -x))
        return nums
# @lc code=end

