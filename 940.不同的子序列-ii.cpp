/*
 * @lc app=leetcode.cn id=940 lang=cpp
 *
 * [940] 不同的子序列 II
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int distinctSubseqII(string s) {
        const int MOD = 1e9+7;
        vector<int> g(26, 0);
        int n = s.size();
        for (int i = 0; i < n; i++) {
            int total = 1;
            for (int j = 0; j < 26; j++) {
                total = (total + g[j]) % MOD;
            }
            g[s[i] - 'a'] = total;
        }
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            ans = (ans + g[i]) % MOD;
        }
        return ans;
    }
};
// @lc code=end

