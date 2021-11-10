# -*- coding: UTF-8 -*-
#
# @lc app=leetcode.cn id=335 lang=python3
#
# [335] 路径交叉
#

# @lc code=start
import collections
from typing import List
from sortedcontainers import SortedList, SortedSet

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        if n < 4: return False
        # 当前所在的位置
        pos = [0, 0]
        # 使用哈希表记录垂直与x、y轴上的线段
        xsegments, ysegments = collections.defaultdict(lambda:SortedList()), collections.defaultdict(lambda:SortedList())
        # 有线段的x点集合和有线段的y点集合
        xlist, ylist = SortedSet(), SortedSet()
        visited = collections.defaultdict(lambda:collections.defaultdict(lambda: False))
        visited[0][0] = True

        # 找到arr中在[l, r]区间内的所有元素
        def find(arr: SortedList, l: int, r: int) -> List[int]:
            if l > r: l, r = r, l
            ans = list(arr.irange(l, r))
            return ans
        

        # 判断数字是否在线段内
        def insegements(segments: SortedList, a: int) -> bool:
            n = len(segments)
            l, r = 0, n - 1
            
            while l <= r:
                mid = (l + r + 1) >> 1
                if segments[mid][0] <= a <= segments[mid][1]:
                    return True
                elif segments[mid][1] < a:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        
        # 判断区间是否存在重复
        def isCrossing(segments: SortedList, l: int, r: int) -> bool:
            if l > r: l, r = r, l
            n = len(segments)
            sl = SortedList([x[0] for x in list(segments)])
            index = sl.bisect_left(l)
            # print(index)
            if index < n:
                if segments[index][0] <= r:
                    return True
                elif index > 0 and segments[index - 1][0] <= l <= segments[index - 1][1]:
                    return True

            return False


        # 检测两点之间是否会穿过线段
        def check(pre: List[int], cur: List[int]):
            if visited[cur[0]][cur[1]]: return True
            if pre[0] == cur[0]:
                # 判断是否会覆盖已有的线段
                if len(xsegments[pre[0]]) > 0 and isCrossing(xsegments[pre[0]], pre[1], cur[1]):
                    return True
                # 判断是否传过平行与y轴的线段
                arry = find(ylist, pre[1], cur[1])
                for y in arry:
                    if y == pre[1]: continue
                    if insegements(ysegments[y], cur[0]): return True
                
            elif pre[1] == cur[1]:
                # 判断是否会覆盖已有的线段
                if len(ysegments[pre[1]]) > 0 and isCrossing(ysegments[pre[1]], pre[0], cur[0]):
                    return True
                # 判断是否传过平行与x轴的线段
                arrx = find(xlist, pre[0], cur[0])
                for x in arrx:
                    if x == pre[0]: continue
                    if insegements(xsegments[x], cur[1]): return True
                
            return False

        for i in range(n):
            old_pos = [pos[0], pos[1]]
            if i % 4 == 0:
                # 向上走，判断会不会穿过
                pos[1] += distance[i]
                if check(old_pos, pos): return True
                xlist.add(pos[0])
                xsegments[pos[0]].add([old_pos[1], pos[1]])
            elif i % 4 == 1:
                # 向左走，判断会不会穿过
                pos[0] -= distance[i]
                if check(old_pos, pos): return True
                ylist.add(pos[1])
                ysegments[pos[1]].add([pos[0], old_pos[0]])
            elif i % 4 == 2:
                # 向下走，判断会不会穿过
                pos[1] -= distance[i]
                if check(old_pos, pos): return True
                xlist.add(pos[0])
                xsegments[pos[0]].add([pos[1], old_pos[1]])
            elif i % 4 == 3:
                # 向右走，判断会不会穿过
                pos[0] += distance[i]
                if check(old_pos, pos): return True
                ylist.add(pos[1])
                ysegments[pos[1]].add([old_pos[0], pos[0]])
            visited[pos[0], pos[1]] = True
            
        return False

# @lc code=end

solution = Solution()
# print('True' if solution.isSelfCrossing([1,1,2,1,2]) else 'False')
# print('True' if solution.isSelfCrossing([2,1,1,2]) else 'False')
# print('True' if solution.isSelfCrossing([1,2,3,4]) else 'False')
print('True' if solution.isSelfCrossing([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6]) else 'False')