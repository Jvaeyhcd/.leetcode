#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
from bisect import bisect_left
from curses.ascii import isalpha
from itertools import combinations, permutations
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        arr = [a.lower() for a in s]
        ans = []
        indexs = []
        for i, c in enumerate(arr):
            if c.isalpha():
                indexs.append(i)
        for l in range(0, len(indexs) + 1):
            for a in combinations(indexs, l):
                new_arr = arr.copy()
                for i in a:
                    new_arr[i] = new_arr[i].upper()
                ans.append(''.join(new_arr))
        return ans
# @lc code=end