#
# @lc app=leetcode.cn id=1441 lang=python3
#
# [1441] 用栈操作构建数组
#

# @lc code=start
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr = []
        num = 0
        for i in target:
            arr.append('Push')
            for j in range(i - num - 1):
                arr.append('Pop')
                arr.append('Push')
            num = i
        return arr
# @lc code=end

