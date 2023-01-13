#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
from typing import List


class FenwickTree:

    def __init__(self, n):
        self.bit_arr = [0 for _ in range(n + 1)]


    def update(self, idx: int, delta: int):
        n = len(self.bit_arr)
        while idx < n:
            self.bit_arr[idx] += delta
            idx += self.lowbit(idx)


    def query(self, idx: int) -> int:
        ans = 0
        while idx:
            ans += self.bit_arr[idx]
            idx -= self.lowbit(idx)
        return ans


    def lowbit(self, x: int) -> int:
        return x & -x


class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        all_nums = set(nums)
        for num in nums:
            all_nums.add(num * 2)
        n = len(all_nums)
        mp = {num: i + 1 for num, i in zip(sorted(list(all_nums)), range(n))}
        
        ans = 0
        BIT = FenwickTree(n)
        for num in nums:
            left, right = mp[num * 2], n
            ans += (BIT.query(right) - BIT.query(left))
            BIT.update(mp[num], 1)
        return ans
        

    # 归并排序
    # def reversePairs(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     return self.merge_reversePairs(nums, 0, len(nums) - 1)
    # 
    # 
    # def merge_reversePairs(self, nums: List[int], left: int, right: int) -> int:
    #     if left == right:
    #         return 0
    #     mid = (left + right) >> 1
    #     n1 = self.merge_reversePairs(nums, left, mid)
    #     n2 = self.merge_reversePairs(nums, mid + 1, right)
    #     res = n1 + n2
    # 
    #     # 统计下标对的数量
    #     i, j = left, mid + 1
    #     while i <= mid:
    #         while j <= right and nums[i] > 2 * nums[j]:
    #             j += 1
    #         res += (j - mid - 1)
    #         i += 1
        
    #     # 合并排序的数组
    #     arr = []
    #     p1, p2 = left, mid + 1
    #     while p1 <= mid or p2 <= right:
    #         if p1 > mid:
    #             arr.append(nums[p2])
    #             p2 += 1
    #         elif p2 > right:
    #             arr.append(nums[p1])
    #             p1 += 1
    #         else:
    #             if nums[p1] < nums[p2]:
    #                 arr.append(nums[p1])
    #                 p1 += 1
    #             else:
    #                 arr.append(nums[p2])
    #                 p2 += 1
        
    #     for i in range(len(arr)):
    #         nums[left + i] = arr[i]
        
    #     return res

# @lc code=end

