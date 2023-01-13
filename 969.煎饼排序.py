#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
#

# @lc code=start
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)):
            # print(arr)
            x = arr.index(len(arr))
            # print(x)
            res.append(x+1)
            res.append(len(arr))
            arr = (arr[:x+1][::-1]+arr[x+1:])[::-1][:-1]
            
        return res
# @lc code=end

arr = [3,2,4,1]
print(arr[:-1])