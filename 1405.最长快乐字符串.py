#
# @lc app=leetcode.cn id=1405 lang=python3
#
# [1405] 最长快乐字符串
#

# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        cnts = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            cnts.sort(key=lambda x: -x[0])
            flag = False
            for i, (c, ch) in enumerate(cnts):
                if c <= 0:
                    break
                if len(ans) > 1 and ans[-2] == ch and ans[-1] == ch:
                    continue
                ans.append(ch)
                cnts[i][0] -= 1
                flag = True
                break
            if not flag:
                return ''.join(ans)
        


# @lc code=end

