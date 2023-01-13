#
# @lc app=leetcode.cn id=564 lang=python3
#
# [564] 寻找最近的回文数
#

# @lc code=start
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        if l == 1:
            return str(int(n) - 1) if n != '0' else '1'
        arr = list(n)
        li, ri = 0, l - 1
        while li < ri:
            arr[ri] = arr[li]
            li += 1
            ri -= 1
        return ''.join(arr)
        


# @lc code=end

solution = Solution()
n = '20'
print(solution.nearestPalindromic(n))