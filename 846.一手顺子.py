#
# @lc app=leetcode.cn id=846 lang=python3
#
# [846] 一手顺子
#

# @lc code=start
from typing import Counter, List
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False
        cnts = Counter(hand)
        
        hand.sort()
        for x in hand:
            if cnts[x] == 0: continue
            for num in range(x, x + groupSize):
                if cnts[num] == 0:
                    return False
                cnts[num] -= 1
        return True
# @lc code=end

# 优先队列
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False
        cnts = Counter(hand)
        keys = list(cnts.keys())
        heapq.heapify(keys)
        group = []
        arr = []
        while keys:
            top = heapq.heappop(keys)
            if not group or group[-1] == top - 1:
                group.append(top)
                cnts[top] -= 1
                if cnts[top] > 0:
                    heapq.heappush(keys, top)
            else:
                arr.append(top)
                    
            if len(group) == groupSize:
                for a in arr: 
                    if cnts[a] > 0: heapq.heappush(keys, a)
                arr = []
                group = []
        return True if not arr else False