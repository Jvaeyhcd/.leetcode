#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#

# @lc code=start
# from typing import List
# from bisect import bisect_right


# class Solution:
#     def findRadius(self, houses: List[int], heaters: List[int]) -> int:
#         heaters.sort()
#         ans = 0
#         for house in houses:
#             j = bisect_right(heaters, house)
#             i = j - 1
#             right = heaters[j] - house if j < len(heaters) else float('inf')
#             left = house - heaters[i] if i >= 0 else float('inf')
#             ans = max(ans, min(left, right))
#         return ans

from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()

        ans, j = 0, 0
        for house in houses:
            distance = abs(house - heaters[j])
            while j + 1 < len(heaters) and abs(house - heaters[j]) >= abs(house - heaters[j + 1]):
                j += 1
                distance = min(distance, abs(house - heaters[j]))
            ans = max(ans, distance)
        return ans

# @lc code=end

