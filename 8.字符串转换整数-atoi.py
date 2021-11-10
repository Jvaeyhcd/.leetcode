#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        positive = True
        flag = ''
        N = len(s)
        ans = ''
        for i in range(N):
            if s[i] == '-':
                if flag == '' and ans == '':
                    flag = '-'
                else:
                    break
                positive = False
            elif s[i] == '+':
                if flag == '' and ans == '':
                    flag = '+'
                else:
                    break
                positive = True
            elif s[i] in '0123456789':
                ans += s[i]
            elif s[i] == ' ':
                if ans != '':
                    break
                if flag != '':
                    break
            else:
                break
        if ans == '':
            return 0
        ans = int(ans)
        if not positive:
            ans = -ans
        
        if ans < -2147483648:
            ans = -2147483648
        elif ans > 2147483647:
            ans = 2147483647
        
        return ans
                
# @lc code=end

