#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#

# @lc code=start
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        indexs = {p[0]: i for i, p in enumerate(pieces)}
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] not in indexs:
                return False
            p = pieces[indexs[arr[i]]]
            if arr[i: i + len(p)] != p:
                return False
            i += len(p)
        return True
# @lc code=end

