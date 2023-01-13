#
# @lc app=leetcode.cn id=850 lang=python3
#
# [850] 矩形面积 II
#

# @lc code=start
from bisect import bisect_left
from typing import List

class Node:
    def __init__(self):
        self.cover = 0
        self.length = 0
        self.max_length = 0


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        hbound = set()
        for rect in rectangles:
            hbound.add(rect[1])
            hbound.add(rect[3])
        
        hbound = sorted(hbound)
        m = len(hbound)

        tree = [Node() for _ in range(m * 4 + 1)]

        def build(idx: int, l: int, r: int):
            tree[idx].cover = tree[idx].length = 0
            if l == r:
                tree[idx].max_length = hbound[l] - hbound[l - 1]
                return
            
            mid = (l + r) >> 1
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)
            tree[idx].max_length = tree[idx * 2].max_length + tree[idx * 2 + 1].max_length

        def pushup(idx: int, l: int, r: int):
            if tree[idx].cover > 0:
                tree[idx].length = tree[idx].max_length
            elif l == r:
                tree[idx].length = 0
            else:
                tree[idx].length = tree[idx * 2].length + tree[idx * 2 + 1].length
        
        def update(idx: int, l: int, r: int, ul, ur: int, diff: int):
            if l > ur or r < ul:
                return
            if ul <= l and r <= ur:
                tree[idx].cover += diff
                pushup(idx, l, r)
                return
            
            mid = (l + r) >> 1
            update(idx * 2, l, mid, ul, ur, diff)
            update(idx * 2 + 1, mid + 1, r, ul, ur, diff)
            pushup(idx, l, r)

        build(1, 1, m - 1)
        
        sweep = list()
        for i, rect in enumerate(rectangles):
            sweep.append((rect[0], i, 1))
            sweep.append((rect[2], i, -1))
        sweep.sort()

        ans = i = 0
        while i < len(sweep):
            j = i
            while j + 1 < len(sweep) and sweep[i][0] == sweep[j + 1][0]:
                j += 1
            if j + 1 == len(sweep):
                break
            for k in range(i, j + 1):
                _, idx, diff = sweep[k]
                left = bisect_left(hbound, rectangles[idx][1]) + 1
                right = bisect_left(hbound, rectangles[idx][3])
                update(1, 1, m - 1, left, right, diff)
            ans += tree[1].length * (sweep[j + 1][0] - sweep[j][0])
            i = j + 1

        return ans % (10 ** 9 + 7)
# @lc code=end

