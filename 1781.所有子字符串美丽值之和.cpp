/*
 * @lc app=leetcode.cn id=1781 lang=cpp
 *
 * [1781] 所有子字符串美丽值之和
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int beautySum(string s) {
        int n = s.size();
        vector<vector<int>> f(n + 1, vector<int>(26));
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < 26; j++) {
                f[i][j] = f[i - 1][j];
            }
            f[i][s[i - 1] - 'a'] += 1;
        }
        
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i; j <= n; j++) {
                int mind = n, maxd = 0;
                for (int a = 0; a < 26; a++) {
                    int d = f[j][a] - f[i - 1][a];
                    if (d < mind && d != 0) mind = d;
                    if (d > maxd) maxd = d;
                }
                ans += (maxd - mind);
            }
        }
        return ans;
    }
};
// @lc code=end

