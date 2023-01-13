/*
 * @lc app=leetcode.cn id=902 lang=cpp
 *
 * [902] 最大为 N 的数字组合
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int atMostNGivenDigitSet(vector<string>& digits, int n) {
        string s = to_string(n);
        int m = s.size(), dp[m];
        memset(dp, -1, sizeof(dp));

        function<int(int, int, int)> dfs = [&](int i, int isLimit, int isNum) {
            if (i == m) return isNum;
            if (!isLimit && isNum && dp[i] >= 0) return dp[i];
            int res = 0;
            if (!isNum) {
                res = dfs(i + 1, 0, 0);
            }
            char up = isLimit ? s[i] : '9';
            for (auto &d: digits) {
                if (d[0] > up) break;
                res += dfs(i + 1, isLimit && d[0] == up, 1);
            }
            if (!isLimit && isNum) dp[i] = res;
            return res;
        };

        return dfs(0, 1, 0);
    }
};
// @lc code=end

