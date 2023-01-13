/*
 * @lc app=leetcode.cn id=790 lang=cpp
 *
 * [790] 多米诺和托米诺平铺
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    typedef long long ll;
    const int MOD = 1e9+7;
    int numTilings(int n) {
        if (n == 1) return 1;
        ll a = 0, b = 0, c = 0, d = 1;
        for (int i = 1; i <= n; i++) {
            ll aa = d;
            ll bb = (a + c) % MOD;
            ll cc = (a + b) % MOD;
            ll dd = (a + b + c + d) % MOD;
            a = aa, b = bb, c = cc, d = dd;
        }
        return d;
    }
};
// @lc code=end

