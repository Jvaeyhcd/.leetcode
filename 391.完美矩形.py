#
# @lc app=leetcode.cn id=391 lang=python3
#
# [391] 完美矩形
#

# @lc code=start
# 方法二：扫描线
from typing import List
from functools import cmp_to_key


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        n = len(rectangles)
        rs = [(0, 0, 0, 1) for _ in range(n * 2)]
        for i in range(n):
            xi, yi, ai, bi = rectangles[i][0], rectangles[i][1], rectangles[i][2], rectangles[i][3]
            rs[2 * i] = (xi, yi, bi, 1)
            rs[2 * i + 1] = (ai, yi, bi, -1)
        
        def cmp(a, b):
            if a[0] != b[0]: return a[0] - b[0]
            return a[1] - b[1] 

        rs = sorted(rs, key=cmp_to_key(cmp))

        l = 0
        while l < 2 * n:
            r = l
            # 分别存储相同横坐标下「左边的线段」和「右边的线段」
            arr1, arr2 = [], []
            # 找到横坐标相同的部分
            while r < 2 * n and rs[r][0] == rs[l][0]:
                r += 1
            for i in range(l, r):
                cur = [rs[i][1], rs[i][2]]
                arr = arr1 if rs[i][3] == 1 else arr2
                if not arr or len(arr) == 0:
                    arr.append(cur)
                else:
                    prev = arr[-1]
                    if cur[0] < prev[1]:
                        # 存在重叠
                        return False
                    elif cur[0] == prev[1]:
                        # 首位相连
                        prev[1] = cur[1]
                    else:
                        arr.append(cur)

            if l > 0 and r < 2 * n:
                # 若不是完美矩形的边缘竖边，检查是否成对出现
                if len(arr1) != len(arr2):
                    return False
                for i in range(len(arr1)):
                    if arr1[i][0] == arr2[i][0] and arr1[i][1] == arr2[i][1]: continue
                    return False
            else:
                # 若是完美矩形的边缘竖边，检查是否形成完整的一段
                if len(arr1) + len(arr2) != 1:
                    return False
            l = r
        return True
        
        
# @lc code=end

# 方法一：哈希表找规律
# import collections
# from typing import List


# class Solution:
#     def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
#         area, minX, minY, maxX, maxY = 0, rectangles[0][0], rectangles[0][1], rectangles[0][2], rectangles[0][3]
#         cnts = collections.defaultdict(lambda:0)

#         for xi, yi, ai, bi in rectangles:
#             minX = min(minX, xi)
#             minY = min(minY, yi)
#             maxX = max(maxX, ai)
#             maxY = max(maxY, bi)

#             cnts[(xi, yi)] += 1
#             cnts[(xi, bi)] += 1
#             cnts[(ai, yi)] += 1
#             cnts[(ai, bi)] += 1
        
#             area += (ai - xi) * (bi - yi)
        
#         # 判断所有矩形的面积和是否与完美矩形相等
#         if area != (maxX - minX) * (maxY - minY):
#             return False
        
#         # 完美矩形的四个顶点只能出现一次
#         points = [(minX, minY), (minX, maxY), (maxX, minY), (maxX, maxY)]
#         for p in points:
#             if cnts[p] != 1:
#                 return False
        
#         # 矩形的其他顶点只能出现2次或4次
#         for k, v in cnts.items():
#             if v > 4 or (v % 2 != 0 and k not in points):
#                 return False
        
#         return True