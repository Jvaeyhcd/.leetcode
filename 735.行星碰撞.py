#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 行星碰撞
#

# @lc code=start
from typing import List


class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        n = len(arr)
        queue = []
        for i in range(n - 1):
            if arr[i] > 0 and arr[i + 1] < 0:
                queue.append(i)

        flag = len(queue) > 0
        
        while queue:
            for _ in range(len(queue)):
                i = queue.pop(0)
                a = arr[i]
                if a > 0:
                    if i + 1 >= n or arr[i + 1] > 0:
                        continue
                    elif arr[i + 1] == 0:
                        arr[i] = 0
                        arr[i + 1] = a
                        queue.append(i + 1)
                    elif arr[i + 1] < 0:
                        b = arr[i + 1]
                        diff = abs(a) - abs(b)
                        if diff == 0:
                            arr[i] = 0
                            arr[i + 1] = 0
                        elif diff > 0:
                            arr[i] = 0
                            arr[i + 1] = a
                            queue.append(i + 1)
                        else:
                            arr[i] = b
                            arr[i + 1] = 0
                            queue.append(i)
                elif a < 0:
                    if i - 1 < 0 or arr[i - 1] < 0:
                        continue
                    elif arr[i - 1] == 0:
                        arr[i] = 0
                        arr[i - 1] = a
                        queue.append(i - 1)
                    elif arr[i - 1] > 0:
                        b = arr[i - 1]
                        diff = abs(b) - abs(a)
                        if diff == 0:
                            arr[i - 1] = 0
                            arr[i] = 0
                        elif diff > 0:
                            arr[i - 1] = 0
                            arr[i] = b
                            queue.append(i)
                        else:
                            arr[i - 1] = a
                            arr[i] = 0
                            queue.append(i - 1)
        
        ans = [a for a in arr if a != 0]
        # print(ans)
        if flag:
            return self.asteroidCollision(ans)
        return ans

# @lc code=end

solution = Solution()
arr = [5,10,-5]
# arr = [10,2,-5]
arr = [1,1,-1,-2]
arr = [100,-96,98,12,-16,-50,85,9,-52,-91,-3,-84,-26,-26,-34,-62,64,-70,49,-28,-61,-85,-62,-68,30,72,52,-14,81,-61,-43,-65,-40,-5,64,-58,16]
arr = [64,-45,-100,-93,-52,-88,27,-19,-96,28,24,66,-4,76,52,-4,100,95,44,-69,-48,51,87,77,49,-92,-85,8,9,76,22,76,-36,-91,-58,-77,-52,67,19,-43,-24,86,-91,-1,83,-60,-53,40,-68,25,-42,6,91,-95,10,-42,-79,16,35,-30,-49,-100,35,100,-96,98,12,-16,-50,85,9,-52,-91,-3,-84,-26,-26,-34,-62,64,-70,49,-28,-61,-85,-62,-68,30,72,52,-14,81,-61,-43,-65,-40,-5,64,-58,16]
print(solution.asteroidCollision(arr))