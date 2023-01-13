#
# @lc app=leetcode.cn id=670 lang=python3
#
# [670] 最大交换
#

# @lc code=start


class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        max_i = n - 1
        i1 = i2 = -1
        for i in range(n - 1, -1, -1):
            if s[i] > s[max_i]:
                max_i = i
            elif s[i] < s[max_i]:
                i1, i2 = i, max_i
        
        if i1 < 0:
            return num
        s[i1], s[i2] = s[i2], s[i1]
        return int(''.join(s))
# @lc code=end

solution = Solution()
num = 98368
num = 2736
# num = 9973
num = 1993
print(solution.maximumSwap(num))