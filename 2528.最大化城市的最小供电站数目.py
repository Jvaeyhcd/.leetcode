#
# @lc app=leetcode.cn id=2528 lang=python3
#
# [2528] 最大化城市的最小供电站数目
#

# @lc code=start
from typing import List


class Solution:
    def maxPower(self, stations: List[int], R: int, K: int) -> int:
        n = len(stations)

        def check(LIM: int) -> bool:
            vec = []
            for p in stations: vec.append(p)

            # 初始化滑动窗口的和
            sm = 0
            for i in range(min(R + 1, n)): sm += vec[i]

            # 表示还有几个供电站可以新建
            rem = K
            # 从左到右计算每个电站的电量，同时维护滑动窗口[l, r]
            i, l, r = 0, 0, R
            while True:
                if sm < LIM:
                    # 当前城市电量不足
                    delta = LIM - sm
                    # 新供电站不够，返回False
                    if delta > rem: return False
                    # 新供电站足够，建在滑动窗口最右边
                    rem -= delta
                    vec[r] += delta
                    sm += delta
                if i == n - 1: break

                # 滑动窗口向前移动一个城市
                if i >= R:
                    sm -= vec[l]
                    l += 1
                if r != n - 1:
                    sm += vec[r + 1]
                    r += 1
                i += 1
            return True

        low, high = 0, int(2e10)
        while low + 1 != high:
            mid = (low + high) >> 1
            if check(mid):
                low = mid
            else:
                high = mid
        return low


# @lc code=end

