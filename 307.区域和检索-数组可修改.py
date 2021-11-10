#
# @lc app=leetcode.cn id=307 lang=python
#
# [307] 区域和检索 - 数组可修改
#

# @lc code=start
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.nums = nums
        self.BIT = FenwickTree(nums)


    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.BIT.update(index + 1, val - self.nums[index])
        self.nums[index] = val


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.BIT.range_sum(left + 1, right + 1)

class FenwickTree(object):

    def __init__(self, n):
        self.bit_arr = [0] * (n + 1)

    def __init__(self, nums):
        n = len(nums)
        self.bit_arr = [0] * (n + 1)
        for i in range(len(nums)):
            self.bit_arr[i + 1] = nums[i]
        
        for i in range(1, n + 1):
            j = i + self.lowbit(i)
            if j < n + 1:
                self.bit_arr[j] += self.bit_arr[i]
    
    def update(self, idx, delta):
        while idx < len(self.bit_arr):
            self.bit_arr[idx] += delta
            idx += self.lowbit(idx)
    
    def prefix_sum(self, idx):
        ans = 0
        while idx:
            ans += self.bit_arr[idx]
            idx -= self.lowbit(idx)
        return ans
    
    def range_sum(self, l, r):
        if l == 0:
            return self.prefix_sum(r)
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

    def lowbit(self, x):
        return x & -x


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

