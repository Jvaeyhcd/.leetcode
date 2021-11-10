#
# @lc app=leetcode.cn id=273 lang=python3
#
# [273] 整数转换英文表示
#

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        singles = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['', 'Thousand', 'Million', 'Billion']

        def helper(num):
            if num < 10:
                return [singles[num]]
            elif num < 20:
                return [teens[num - 10]]
            elif num < 100:
                ans = [tens[num // 10]]
                if num % 10:
                    ans += helper(num % 10)
                return ans
            elif num < 1000:
                ans = [singles[num // 100], 'Hundred']
                if num % 100:
                    ans += helper(num % 100)
                return ans
        
        res = []
        unit = 1000000000
        for i in range(3, -1, -1):
            cur = num // unit
            if cur != 0:
                num -= cur * unit
                res += helper(cur)
                if thousands[i] != '':
                    res += [thousands[i]]
            unit //= 1000
        return ' '.join(res)
        print(helper(0))
        # print(helper(1))
        # print(helper(11))
        # print(helper(19))
        # print(helper(20))
        # print(helper(21))
        # print(helper(101))

# @lc code=end

