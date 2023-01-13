#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#

# @lc code=start
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        self.BIT = FenwickTree(n)
        for i in range(n):
            self.BIT.update(i + 1, nums[i])


    def update(self, index: int, val: int) -> None:
        self.BIT.update(index + 1, val - self.nums[index])
        self.nums[index] = val


    def sumRange(self, left: int, right: int) -> int:
        return self.BIT.query(right + 1) - self.BIT.query(left)


class FenwickTree:
    
    def __init__(self, n: int):
        self.bit_arr = [0] * (n + 1)


    def lowbit(self, x: int) -> int:
        return x & -x

    
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


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

