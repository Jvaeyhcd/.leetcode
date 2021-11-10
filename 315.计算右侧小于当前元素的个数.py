#
# @lc app=leetcode.cn id=315 lang=python
#
# [315] 计算右侧小于当前元素的个数
#

# @lc code=start
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        hash_table = {v: i for i, v in enumerate(sorted(nums))}
        BIT = FenwickTree([0] * n)

        ans = []
        for i in range(n, 0, -1):
            ans.append(BIT.prefix_sum(hash_table[nums[i - 1]]))
            BIT.update(hash_table[nums[i - 1]] + 1, 1)
        return ans[::-1]


class FenwickTree(object):

    # def __init__(self, n):
    #     self.bit_arr = [0] * (n + 1)
    
    def __init__(self, nums):
        n = len(nums)
        self.bit_arr = [0] * (n + 1)
        for i in range(n):
            self.bit_arr[i + 1] = nums[i]
        
        for i in range(1, n + 1):
            j = i + self.lowbit(i)
            if j < n + 1:
                self.bit_arr[j] += self.bit_arr[i]
    
    def update(self, idx, delta):
        n = len(self.bit_arr)
        while idx < n:
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
# @lc code=end

