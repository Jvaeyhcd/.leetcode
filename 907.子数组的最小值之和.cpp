/*
 * @lc app=leetcode.cn id=907 lang=cpp
 *
 * [907] 子数组的最小值之和
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:

    typedef long long ll;
    const int MOD = int(1e9+7);

    int sumSubarrayMins(vector<int>& arr) {
        ll n = arr.size();
        vector<ll> left(n, 0), right(n, 0);
        stack<ll> st;

        for (ll i = 0; i < n; i++) {
            while (!st.empty() && arr[i] <= arr[st.top()]) {
                st.pop();
            }
            left[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }

        while (!st.empty()) st.pop();
        for (ll i = n - 1; i >= 0; i--) {
            while (!st.empty() && arr[i] < arr[st.top()]) {
                st.pop();
            }
            right[i] = st.empty() ? n : st.top();
            st.push(i);
        }

        ll ans = 0;
        for (ll i = 0; i < n; i++) {
            ans += (i - left[i]) * (right[i] - i) * arr[i];
            ans %= MOD;
        }
        return int(ans);
    }
};
// @lc code=end

