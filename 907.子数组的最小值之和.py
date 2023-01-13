#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#

# @lc code=start
from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        prev = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            prev[i] = -1 if not stack else stack[-1]
            stack.append(i)
        
        stack = []
        next = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            next[i] = n if not stack else stack[-1]
            stack.append(i)
        
        ans = 0
        MOD = 10**9+7
        for i in range(n):
            ans += (i - prev[i]) * (next[i] - i) * arr[i]
            ans %= MOD
        return ans



# @lc code=end

solution = Solution()
arr = [3,1,2,4]
arr = [11,81,94,43,3]
print(solution.sumSubarrayMins(arr))