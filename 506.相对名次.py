#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
from typing import List
import heapq
import collections


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = score
        score = [-num for num in score]
        hash_map = collections.defaultdict(int)
        heapq.heapify(score)
        rank = 1
        while score:
            num = -heapq.heappop(score)
            hash_map[num] = rank
            rank += 1

        ans = []
        for num in arr:
            if hash_map[num] == 1:
                ans.append('Gold Medal')
            elif hash_map[num] == 2:
                ans.append('Silver Medal')
            elif hash_map[num] == 3:
                ans.append('Bronze Medal')
            else:
                ans.append(str(hash_map[num]))

        return ans


# @lc code=end

