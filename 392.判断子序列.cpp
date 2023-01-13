/*
 * @lc app=leetcode.cn id=392 lang=cpp
 *
 * [392] 判断子序列
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int m = s.size(), n = t.size();
        vector<vector<int>> dp(n + 1, vector<int>(26, 0));
        for (int i = 0; i < 26; i++) {
            dp[n][i] = n;
        }

        for (char c = 'a'; c <= 'z'; c++) {
            for (int i = n - 1; i >= 0; i--) {
                if (t[i] == c) {
                    dp[i][c - 'a'] = i;
                } else {
                    dp[i][c - 'a'] = dp[i + 1][c - 'a'];
                }
            }
        }
        int i = 0;
        for (char c: s) {
            if (dp[i][c - 'a'] == n) return false;
            i = dp[i][c - 'a'] + 1;
        }
        return true;
    }
};
// @lc code=end

