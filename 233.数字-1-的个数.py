#
# @lc app=leetcode.cn id=233 lang=python
#
# [233] 数字 1 的个数
#

# @lc code=start
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 将数字的每一位取出来放在数组中
        nums = []
        while n:
            nums.append(n % 10)
            n /= 10
        # 数位数组逆序，高位在前，地位在后
        self.nums = nums[::-1]
        print self.nums
        # dp[i][j]代表前i位出现1的次数为j的个数
        self.dp = [[-1] * 20 for _ in range(20)]
        return self.dfs(0, 0, 1)
        
    # pos当前位数
    # st为1的个数
    def dfs(self, pos, st, limit):
        if pos > len(self.nums) - 1:
            return st
        
        if not limit and self.dp[pos][st] != -1:
            return self.dp[pos][st]
        
        uppper = self.nums[pos] if limit else 9
        res = 0
        for x in range(uppper + 1):
            if x == 1:
                res += self.dfs(pos + 1, st + 1, limit and x == uppper)
            else:
                res += self.dfs(pos + 1, st, limit and x == uppper)
        
        if not limit:
            self.dp[pos][st] = res
        
        return res
        

# @lc code=end

