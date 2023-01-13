/*
 * @lc app=leetcode.cn id=2376 lang=cpp
 *
 * [2376] 统计特殊整数
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int countSpecialNumbers(int n) {
        string s = to_string(n);
        int m = s.size(), dp[m][1 << 10];
        memset(dp, -1, sizeof(dp));

        function<int(int, int, int, int)> dfs = [&](int i, int mask, int isLimit, int isNum) {
            if (i == m) return isNum;
            if (!isLimit && isNum && dp[i][mask] >= 0) return dp[i][mask];
            int res = 0;
            if (!isNum) res = dfs(i + 1, mask, 0, 0);
            int up = isLimit ? s[i] - '0' : 9;
            for (int d = 1 - isNum; d <= up; d++) {
                if (((mask >> d) & 1) == 0) {
                    res += dfs(i + 1, mask | (1 << d), isLimit && d == up, 1);
                }
            }
            if (!isLimit && isNum) dp[i][mask] = res;
            return res;
        };

        return dfs(0, 0, 1, 0);
    }
};
// @lc code=end

