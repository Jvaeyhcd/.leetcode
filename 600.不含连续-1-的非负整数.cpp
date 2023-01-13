/*
 * @lc app=leetcode.cn id=600 lang=cpp
 *
 * [600] 不含连续1的非负整数
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int findIntegers(int n) {
        vector<int> bits;
        while (n) {
            bits.push_back(n & 1);
            n >>= 1;
        }
        reverse(bits.begin(), bits.end());

        int m = bits.size(), dp[m + 1][2];
        memset(dp, -1, sizeof(dp));

        function<int(int, int, int)> dfs = [&](int i, int prev1, int isLimit) {
            if (i == m) return 1;
            if (!isLimit && dp[i][prev1] >= 0) return dp[i][prev1];
            int up = isLimit ? bits[i] : 1;
            int res = dfs(i + 1, 0, isLimit && up == 0);
            if (!prev1 && up == 1) {
                res += dfs(i + 1, 1, isLimit);
            }
            if (!isLimit) dp[i][prev1] = res;
            return res;
        };

        return dfs(0, 0, 1);
    }
};
// @lc code=end

