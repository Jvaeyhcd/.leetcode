#
# @lc app=leetcode.cn id=913 lang=python3
#
# [913] 猫和老鼠
#

# @lc code=start
from typing import List
from functools import lru_cache

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:

        @lru_cache(None)
        def search(t: int, x: int, y: int) -> int:
            # 总步数达到了2N，意味着猫和老鼠各走了N步，下一步肯定出现在出现过的位置，那么必然是平局了
            if t == len(graph) * 2: return 0
            # 猫和老鼠出现在了相同的位置，猫获胜
            if x == y: return 2
            # 老鼠进洞了，老鼠获胜
            if x == 0: return 1

            if t % 2 == 0:
                # 当前是老鼠走的时间，如果老鼠能在任意下一步中赢返回老鼠赢
                if any(search(t + 1, nxt_x, y) == 1 for nxt_x in graph[x]):
                    return 1
                # 老鼠任何下一步返回结果是平局，那么返回平局
                if any(search(t + 1, nxt_x, y) == 0 for nxt_x in graph[x]):
                    return 0
                # 否则猫赢
                return 2
            else:
                # 当前是猫走的时间，如果猫能在下一步中赢返回猫赢
                if any(search(t + 1, x, nxt_y) == 2 for nxt_y in graph[y] if nxt_y != 0):
                    return 2
                # 猫任何下一步返回结果是平局，那么返回平局
                if any(search(t + 1, x, nxt_y) == 0 for nxt_y in graph[y] if nxt_y != 0):
                    return 0
                # 否则老鼠赢
                return 1
        return search(0, 1, 2)


# @lc code=end

