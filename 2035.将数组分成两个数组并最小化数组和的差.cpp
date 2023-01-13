/*
 * @lc app=leetcode.cn id=2035 lang=cpp
 *
 * [2035] 将数组分成两个数组并最小化数组和的差
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    typedef long long ll;
    int minimumDifference(vector<int>& nums) {
        int n = nums.size();
        int m = n >> 1;
        map<int, vector<ll>> mp1, mp2;
        ll total = accumulate(nums.begin(), nums.end(), 0);

        mp1[0].push_back(0);
        for (int i = 1; i < (1 << m); i++) {
            ll tot = 0;
            int cnt = 0;
            for (int j = 0; j < m; j++) {
                if (i >> j & 1) {
                    tot += nums[j];
                    cnt += 1;
                }
            }
            mp1[cnt].push_back(tot);
        }
        
        mp2[0].push_back(0);
        for (int i = 0; i < (1 << m); i++) {
            ll tot = 0;
            int cnt = 0;
            for (int j = 0; j < m; j++) {
                if (i >> j & 1) {
                    tot += nums[m + j];
                    cnt += 1;
                }
            }
            mp2[cnt].push_back(tot);
        }

        for (auto &it: mp1) {
            auto& vec = it.second;
            sort(vec.begin(), vec.end());
        }
        ll ans = INT_MAX;

        for (int i = 0; i <= m; i++) {
            auto& vec1 = mp1[i];
            auto& vec2 = mp2[m - i];
            for (auto x: vec2) {
                int id = lower_bound(vec1.begin(), vec1.end(), total / 2 - x) - vec1.begin();
                int y = -1;
                if (id < vec1.size()) {
                    y = vec1[id];
                    ans = min(ans, abs(total - (x + y) - (x + y)));
                }
                if (id > 0) {
                    y = vec1[id - 1];
                    ans = min(ans, abs(total - (x + y) - (x + y)));
                }
            }
        }

        return int(ans);
    }
};
// @lc code=end

