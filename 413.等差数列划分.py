#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#

# @lc code=start
# 动态规划 - 空间压缩到O(1)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        ans, dpi, dpi_1 = 0, 0, 0
        for i in range(1, N - 1):
            if nums[i] * 2 == nums[i - 1] + nums[i + 1]:
                dpi = dpi_1 + 1
            else:
                dpi = 0
            ans += dpi
            dpi_1 = dpi
        return ans

# @lc code=end

# 记忆化DFS递归
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        self.ans = 0
        self.memo = [0] * N
        self.dfs(nums, N - 1)
        return self.ans
    
    def dfs(self, nums: List[int], end: int) -> int:
        if end < 2: return 0
        if self.memo[end] > 0:
            return self.memo[end]
        
        cnt = 0
        if nums[end] - nums[end - 1] == nums[end - 1] - nums[end - 2]:
            cnt = 1 + self.dfs(nums, end - 1)
        else:
            self.dfs(nums, end - 1)
        
        self.memo[end] = cnt
        self.ans += cnt
        return cnt

# 递归
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        self.ans = 0
        self.dfs(nums, N - 1)
        return self.ans
    
    def dfs(self, nums: List[int], end: int) -> int:
        if end < 2: return 0
        cnt = 0
        if nums[end] - nums[end - 1] == nums[end - 1] - nums[end - 2]:
            cnt = 1 + self.dfs(nums, end - 1)
            self.ans += cnt
        else:
            self.dfs(nums, end - 1)
        return cnt

# 动态规划
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        for i in range(1, N - 1):
            if nums[i] * 2 == nums[i - 1] + nums[i + 1]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)

# 暴力
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        def isArithmetic(start: int, end: int) -> bool:
            if end - start < 2: return False
            for i in range(start, end - 1):
                if nums[i + 1] * 2 != nums[i] + nums[i + 2]:
                    return False

            return True
        
        N = len(nums)
        ans = 0
        for i in range(N - 2):
            for j in range(i + 1, N):
                if isArithmetic(i, j):
                    ans += 1
        return ans

# 滑动窗口-双指针
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range(N - 2):
            d = nums[i + 1] - nums[i]
            for j in range(i + 1, N - 1):
                if nums[j + 1] - nums[j] == d:
                    ans += 1
                else:
                    break
        return ans