#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        l, r = 0, n - 1
        arr = list(s)
        while l < r:
            if arr[l].isalpha() and arr[r].isalpha():
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            elif arr[l].isalpha():
                r -= 1
            elif arr[r].isalpha():
                l += 1
            else:
                l += 1
                r -= 1
        ans = ''.join(arr)
        return ans
                
# @lc code=end

