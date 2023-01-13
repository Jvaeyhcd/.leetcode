#
# @lc app=leetcode.cn id=1994 lang=python3
#
# [1994] 好子集的数目
#

# @lc code=start
import functools
from itertools import count
from math import gcd
from typing import Counter, List


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        MOD = 10**9+7
        cnt = Counter(nums)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        
        n = len(primes)
        dp = [0 for _ in range(1 << n)]
        dp[0] = pow(2, cnt[1], MOD)

        for num, occ in cnt.items():
            if num == 1:
                continue
            subset = 0
            flag = True
            for i, prime in enumerate(primes):
                if num % (prime * prime) == 0:
                    flag = False
                    break
                if num % prime == 0:
                    subset |= (1 << i)
            if not flag:
                continue
        
            for mask in range((1 << n) - 1, 0, -1):
                if (mask & subset) == subset:
                    dp[mask] = (dp[mask] + dp[mask ^ subset] * occ) % MOD
        
        return sum(dp[1:]) % MOD
# @lc code=end

solution = Solution()
# nums = [4,2,3,15]
nums = [1,2,3,4]
# nums = [5,10,1,26,24,21,24,23,11,12,27,4,17,16,2,6,1,1,6,8,13,30,24,20,2,19]
print(solution.numberOfGoodSubsets(nums))