#
# @lc app=leetcode.cn id=2334 lang=python3
#
# [2334] 元素值大于变化阈值的子数组
#

# @lc code=start
from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = [-1] * n
        st = []
        for i, v in enumerate(nums):
            while st and nums[st[-1]] >= v:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        
        right = [n] * n
        st = []
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)

        for num, l, r in zip(nums, left, right):
            size = r - l - 1
            if num > threshold // size:
                return size
        return -1
# @lc code=end

