#
# @lc app=leetcode.cn id=420 lang=python3
#
# [420] 强密码检验器
#

# @lc code=start
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        arr = list(password)
        n = len(arr)
        A, B, C = 0, 0, 0
        for ch in arr:
            if 'a' <= ch <= 'z': 
                A = 1
            elif '0' <= ch <= '9':
                B = 1
            elif 'A' <= ch <= 'Z':
                C = 1
        m = A + B + C
        if n < 6:
            return max(6 - n, 3 - m)
        elif n <= 20:
            ans = 0
            i = 0
            while i < n:
                j = i
                while j < n and arr[j] == arr[i]:
                    j += 1
                cnt = j - i
                if cnt >= 3:
                    ans += cnt // 3
                i = j
            return max(ans, 3 - m)
        else:
            ans = 0
            cnts = [0] * 3
            i = 0
            while i < n:
                j = i
                while j < n and arr[j] == arr[i]:
                    j += 1
                cnt = j - i
                if cnt >= 3:
                    ans += cnt // 3
                    cnts[cnt % 3] += 1
                i = j
            
            base = n - 20
            cur = base
            for i in range(3):
                if i == 2:
                    cnts[i] = ans
                if cnts[i] != 0 and cur != 0:
                    t = min(cnts[i] * (i + 1), cur)
                    cur -= t
                    ans -= t // (i + 1)
            return base + max(ans, 3 - m)
# @lc code=end

