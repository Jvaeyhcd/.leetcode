#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        ans = 0
        maxRight = [0] * n
        maxLeft = [0] * n
        maxLeft[0] = height[0]
        maxRight[n - 1] = height[n - 1]

        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])
        
        for i in range(n):
            ans += (min(maxLeft[i], maxRight[i]) - height[i])

        return ans

# @lc code=end

# 暴力解法
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        for i in range(n):
            left_max, right_max = 0, 0
            for j in range(i + 1):
                left_max = max(left_max, height[j])
            
            for j in range(i, n):
                right_max = max(right_max, height[j])
            
            ans += (min(left_max, right_max) - height[i])
        return ans

# 动态规划
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        # 定义二维数组dp
        # dp[i][0]表示下标i左边最大的高度
        # dp[i][1]表示下标i右边最大的高度
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = height[0]
        dp[n - 1][1] = height[n - 1]
        ans = 0

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], height[i])
        
        for i in range(n - 2, -1, -1):
            dp[i][1] = max(dp[i + 1][1], height[i])
        
        for i in range(n):
            ans += (min(dp[i]) - height[i])

        return ans

# 双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        left, right, leftMax, rightMax = 0, n - 1, 0, 0
        ans = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax < rightMax:
                ans += (leftMax - height[left])
                left += 1
            else:
                ans += (rightMax - height[right])
                right -= 1
        return ans

# 单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        n = len(height)
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if not stack:
                    break
                
                left = stack[-1]
                w = i - left - 1
                h = min(height[i], height[left]) - height[top]
                ans += w * h
            stack.append(i)
        return ans