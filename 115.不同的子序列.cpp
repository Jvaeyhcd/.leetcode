/*
 * @lc app=leetcode.cn id=115 lang=cpp
 *
 * [115] 不同的子序列
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    typedef unsigned long long ll;
    int numDistinct(string s, string t) {
        int m = s.size(), n = t.size();
        s = " " + s, t = " " + t;
        vector<vector<ll>> dp(m + 1, vector<ll>(n + 1, 0));
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = dp[i - 1][j];
                if (s[i] == t[j]) {
                    dp[i][j] += dp[i - 1][j - 1];
                }
            }
        }
        return dp[m][n];
    }
};
// @lc code=end

