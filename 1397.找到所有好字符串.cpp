/*
 * @lc app=leetcode.cn id=1397 lang=cpp
 *
 * [1397] 找到所有好字符串
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
    typedef long long ll;
    const int MOD = 1e9+7;

    vector<int> getNextArray(string s) {
        vector<int> next(s.size(), 0);
        int j = 0;
        for (int i = 1; i < s.size(); i++) {
            while (j && s[i] != s[j]) {
                j = next[j - 1];
            }
            if (s[i] == s[j]) {
                j += 1;
            }
            next[i] = j;
        }
        return next;
    }

    int calc(string s, string e) {
        int l1 = s.size(), l2 = e.size(), dp[l1][l2];
        memset(dp, -1, sizeof(dp));
        vector<int> evilNext = getNextArray(e);

        // dfs(i1, i2, isLimit)表示从字符串s从左往右第i1位及其之后数位匹配了i2个e字符串的合法方案数
        function<int(int, int, int)> dfs = [&](int i1, int i2, int isLimit) {
            // 已经匹配了字符串e中所有的字符，返回0
            if (i2 == l2) return 0;
            // 已遍历完s字符串传未发现完全匹配e，返回1
            if (i1 == l1) return 1;
            if (!isLimit && dp[i1][i2] >= 0) return dp[i1][i2];
            ll res = 0;
            char up = isLimit ? s[i1] : 'z';
            for (char d = 'a'; d <= up; d++) {
                int next = i2;
                while (next > 0 && d != e[next]) {
                    next = evilNext[next - 1];
                }
                if (d == e[next]) {
                    next += 1;
                }
                res += dfs(i1 + 1, next, isLimit && d == up);
                res %= MOD;
            }
            if (!isLimit) dp[i1][i2] = res;
            return (int)res;
        };

        return dfs(0, 0, 1);
    }

public:
    int findGoodStrings(int n, string s1, string s2, string evil) {
        return (calc(s2, evil) - calc(s1, evil) + (s1.find(evil) == -1) + MOD) % MOD;
    }
};
// @lc code=end

