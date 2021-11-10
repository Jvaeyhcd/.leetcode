#
# @lc app=leetcode.cn id=488 lang=python3
#
# [488] 祖玛游戏
#

# @lc code=start
from functools import lru_cache
import re

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        ans = self.dfs(board, hand)
        return ans if ans <= len(hand) else -1


    @lru_cache(None)
    def dfs(self, cur_board: str, cur_hand: str) -> int:
        if not cur_board: return 0
        res = 0xf3f3f3f3
        new_board = self.clean(cur_board)
        if new_board == '': return 0
        # print(cur_board, cur_hand, new_board)
        for i in range(len(new_board)):
            for j in range(len(cur_hand)):
                res = min(res, 1 + self.dfs(new_board[:i] + cur_hand[j] + new_board[i:], cur_hand[:j] + cur_hand[j+1:]))
        return res
    
    def clean(self, s: str) -> str:
        n = 1
        while n:
            s, n = re.subn(r'(.)\1{2,}', '', s)
        return s


# @lc code=end

solution = Solution()
# print(solution.findMinStep('RBYYBBRRB', 'YRBGB'))
# print(solution.findMinStep('G', 'GGGGG'))
print(solution.findMinStep('RRGGBBYYWWRRGGBB', 'RGBYW'))