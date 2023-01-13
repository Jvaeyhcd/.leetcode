#
# @lc app=leetcode.cn id=1044 lang=python3
#
# [1044] 最长重复子串
#

# @lc code=start
from typing import List


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ans = ''
        n = len(s)
        l, r = 0, n - 1
        arr = [ord(c) - ord('a') for c in s]

        while l <= r:
            mid = (l + r + 1) >> 1
            x = self.check(arr, s, mid)
            if x != '':
                l = mid + 1
                ans = x
            else:
                r = mid - 1
        return ans

    # Rabin-Karp算法查找字符串中长度为l的重复子串
    def check(self, arr: List[int], s: str, l: int) -> str:
        BASE = 31
        n = len(s)
        power = 1
        hash = 0
        hash_set = set()
        for i in range(l):
            hash = hash * BASE + arr[i]
            power *= BASE
        hash_set.add(hash)
        
        for i in range(l, n):
            hash = hash * BASE + arr[i] - power * arr[i - l]
            if hash in hash_set:
                return s[i-l+1:i+1]
            hash_set.add(hash)
        return ''
        
# @lc code=end

