#
# @lc app=leetcode.cn id=770 lang=python3
#
# [770] 基本计算器 IV
#

# @lc code=start
from typing import List
import collections


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        mp = collections.defaultdict(int)
        for k, v in zip(evalvars, evalints):
            mp[k] = v
        st = []
        
# @lc code=end

