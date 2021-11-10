#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
# 迭代
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(n - 1):
            tmp = ''
            i = 0
            while i < len(ans):
                count = 1
                for j in range(i + 1, len(ans)):
                    if ans[i] == ans[j]:
                        count += 1
                    else:
                        break
                tmp += str(count) + ans[i]
                i += count
            ans = tmp
        return ans
# @lc code=end
# 递归
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        if n == 2: return '11'
        pre = self.countAndSay(n - 1)
        arr = list(pre)
        ans = ''
        N = len(arr)
        i = 0
        while i < N:
            count = 1
            for j in range(i + 1, N):
                if arr[i] == arr[j]: count += 1
                else: break
            ans += (str(count) + arr[i])
            i += count
        return ans