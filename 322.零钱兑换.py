#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
# 记忆化搜索
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = int(1e9)
        self.memo = collections.defaultdict(lambda:0)
        
        # 记忆化搜索
        def dfs(money: int):
            if money < 0: self.memo[money] = -1
            if money == 0: self.memo[money] = 0
            if money in self.memo: return self.memo[money]
            
            mini = INF
            for coin in self.coins:
                res = dfs(money - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            ans = mini if mini < INF else -1
            self.memo[money] = ans
            return ans
        
        self.coins = coins
        if amount == 0:
            return 0
        return dfs(amount)
# @lc code=end

# @lc code=start
# 动态规划
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1: return 0
        INF = int(1e9)
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for money in range(1, amount + 1):
            for coin in coins:
                if coin <= money:
                    dp[money] = min(dp[money], dp[money - coin] + 1)
        
        return dp[amount]
# @lc code=end