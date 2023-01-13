#
# @lc app=leetcode.cn id=1964 lang=python3
#
# [1964] 找出到每个位置为止最长的有效障碍赛跑路线
#

# @lc code=start
from bisect import bisect_right
import collections
from typing import List

class FenwickTree:
    def __init__(self, n: int):
        self.bit_arr = [0] * (n + 1)

    
    def lowbit(self, x: int) -> int:
        return x & (-x)


    def update(self, idx: int, delta: int):
        n = len(self.bit_arr)
        while idx < n:
            self.bit_arr[idx] = max(self.bit_arr[idx], delta)
            idx += self.lowbit(idx)
    

    def query(self, idx: int) -> int:
        ans = 0
        while idx:
            ans = max(ans, self.bit_arr[idx])
            idx -= self.lowbit(idx)
        return ans

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        arr = [k for k, _ in collections.Counter(obstacles).items()]
        n = len(arr)
        BIT = FenwickTree(n)
        h = [i for i in range(n)]
        h.sort(key=lambda x:arr[x])
        mp = collections.defaultdict(int)
        for i in range(n):
            mp[arr[h[i]]] = i + 1
        
        ans = []
        cnt = collections.defaultdict(lambda:0)
        for i, num in enumerate(obstacles):
            index = mp[num]
            res = BIT.query(index)
            ans.append(res + 1)
            BIT.update(index, res + 1)
        return ans

        # ans, stack = [], []
        # for num in obstacles:
        #     if not stack or stack[-1] <= num:
        #         stack.append(num)
        #         ans.append(len(stack))
        #     else:
        #         loc = bisect_right(stack, num)
        #         ans.append(loc + 1)
        #         stack[loc] = num
        # return ans

# @lc code=end
solution = Solution()
obstacles = [2,2,1]
obstacles = [3,1,5,6,4,2]
print(solution.longestObstacleCourseAtEachPosition(obstacles))
