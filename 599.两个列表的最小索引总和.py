#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
from cmath import inf
from typing import List
import heapq


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {k: i for i, k in enumerate(list1)}
        total = inf
        ans = []
        for i, word in enumerate(list2):
            if word in index:
                j = index[word]
                if i + j < total:
                    total = i + j
                    ans = [word]
                elif i + j == total:
                    ans.append(word)
        return ans
# @lc code=end
solution = Solution()
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(solution.findRestaurant(list1, list2))

nums = [1,3,4,5,6,7,8,9,10,22]
nums.remove(22)
print(nums)