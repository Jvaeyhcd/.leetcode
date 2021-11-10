#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        memo = [0] * n
        cur, prev = -1, -1
        # memo[i] 为0代表还未访问，1代表可以拆分为单词，2代表不能拆分为单词
        def dfs(memo: List[int], pos: int, sub: str, cur: int, prev: int):
            # print(pos, sub)
            memo[pos] = 2
            if sub in wordDict:
                memo[pos], sub = 1, ''
                prev = cur
                cur = pos
            
            if prev != -1 and s[prev+1:pos+1] in wordDict:
                memo[pos] = 1

            if pos == n - 1:
                return
            
            dfs(memo, pos + 1, sub + s[pos + 1], cur, prev)
            
        dfs(memo, 0, s[0], cur, prev)
        # print(memo)
        return memo[n - 1] == 1
# @lc code=end
"leetcode"
["leet","code"]
"a"
["leetcode"]
"aaaaa"
["aaaa","aaa"]
"abababa"
["ab","abc","aba"]
"goalspecial"
["go","goal","goals","special"]
