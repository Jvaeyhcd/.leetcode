/*
 * @lc app=leetcode.cn id=862 lang=cpp
 *
 * [862] 和至少为 K 的最短子数组
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    typedef long long ll;
    int shortestSubarray(vector<int>& nums, int k) {
        ll n = nums.size();
        vector<ll> presum(n + 1, 0);
        for (ll i = 0; i < n; i++) {
            presum[i + 1] = presum[i] + nums[i];
        }
        ll ans = n + 1;
        deque<ll> dq;
        for (ll i = 0; i <= n; i++) {
            while (!dq.empty() && presum[i] <= presum[dq.back()]) {
                dq.pop_back();
            }
            while (!dq.empty() && presum[i] - presum[dq.front()] >= k) {
                ll len = i - dq.front();
                dq.pop_front();
                if (len < ans) {
                    ans = len;
                }
            }
            dq.push_back(i);
        }
        return ans == n + 1 ? -1 : (int)ans;
    }
};
// @lc code=end

