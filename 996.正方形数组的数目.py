#
# @lc app=leetcode.cn id=996 lang=python3
#
# [996] 正方形数组的数目
#

# @lc code=start
from typing import List


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        n = len(nums)
        # 所有的排列
        arr = []
        def backtrack(path: List[tuple]):
            if len(path) == n:
                a = [n for _, n in path]
                flag = True
                for i in range(1, len(a)):
                    if not self.isPerfectSquare(a[i - 1] + a[i]):
                        flag = False
                        break

                if flag and a not in arr:
                    arr.append(a)
                return
            for i, num in enumerate(nums):
                if (i, num) not in path:
                    backtrack(path + [(i, num)])
        
        backtrack([])
        return len(arr)
    
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False
# @lc code=end

S = Solution()
nums = [1,17,8]
nums = [2]
nums = [1,1,1,1,1,1,1,1,1,1]
print(S.numSquarefulPerms(nums))