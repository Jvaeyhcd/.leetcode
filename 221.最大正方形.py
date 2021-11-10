#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
# 二进制解法
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        def binary_max_width(num):
            ans = 0
            while num:
                num &= num << 1
                ans += 1
            return ans
        
        nums = [int(''.join(arr), base=2) for arr in matrix]
        width, n = 0, len(nums)
        for i in range(n):
            tmp = nums[i]
            for j in range(i, n):
                tmp &= nums[j]
                w = binary_max_width(tmp)
                h = j - i + 1
                width = max(width, min(w, h))
        return width * width


# @lc code=end

