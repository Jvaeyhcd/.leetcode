#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        LEN = pow(2, n)
        unused = set(i for i in range(LEN) if i != 0)
        ans = [0]

        def backtrack() -> bool:
            if len(ans) >= LEN: return True
            pre = ans[-1]
            for i in range(n):
                next = pre ^ (1 << i)
                if next in unused:
                    unused.remove(next)
                    ans.append(next)
                    if backtrack():
                        return True
                    else:
                        unused.add(next)
                        ans.pop()
            return False
        
        backtrack()

        return ans
# @lc code=end

