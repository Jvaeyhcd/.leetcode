/*
 * @lc app=leetcode.cn id=792 lang=cpp
 *
 * [792] 匹配子序列的单词数
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        int n = s.size();
        vector<vector<int>> dp(n + 1, vector<int>(26, 0));
        for (int i = 0; i < 26; i++) {
            dp[n][i] = n;
        }

        for (int i = n - 1; i >= 0; i--) {
            for (char c = 'a'; c <= 'z'; c++) {
                if (s[i] == c) {
                    dp[i][c - 'a'] = i;
                } else {
                    dp[i][c - 'a'] = dp[i + 1][c - 'a'];
                }
            }
        }

        int ans = 0;
        for (string word: words) {
            int i = 0;
            bool flag = true;
            for (char c: word) {
                if (dp[i][c - 'a'] == n) {
                    flag = false;
                    break;
                }
                i = dp[i][c - 'a'] + 1;
            }
            if (flag) ans += 1;
        }
        return ans;
    }
};
// @lc code=end

