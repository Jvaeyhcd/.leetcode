/*
 * @lc app=leetcode.cn id=1755 lang=cpp
 *
 * [1755] 最接近目标值的子序列和
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    typedef long long ll;
    int minAbsDifference(vector<int>& nums, int goal) {
        int n = nums.size();
        int m = n / 2;
        set<ll> s;
        for (int i = 0; i < (1 << m); i++) {
            ll tot = 0;
            for (int j = 0; j < m; j++) {
                if (i >> j & 1) {
                    tot += nums[j];
                }
            }
            if (tot == goal) return 0;
            s.insert(tot);
        }
        vector<ll> left(s.begin(), s.end());
        ll ans = INT_MAX;
        for (int i = 0; i < (1 << (n - m)); i++) {
            ll tot = 0;
            for (int j = 0; j < n - m; j++) {
                if (i >> j & 1) {
                    tot += nums[m + j];
                }
            }
            int idx = lower_bound(left.begin(), left.end(), goal - tot) - left.begin();
            if (idx == left.size()) {
                idx = left.size() - 1;
            }
            if (idx - 1 >= 0) {
                if (abs(goal - left[idx - 1] - tot) < abs(goal - left[idx] - tot)) {
                    idx = idx - 1;
                }
            }
            if (abs(left[idx] + tot - goal) < ans) {
                ans = abs(left[idx] + tot - goal);
            }
        }
        return ans;
    }
};
// @lc code=end

