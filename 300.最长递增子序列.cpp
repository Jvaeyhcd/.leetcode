/*
 * @lc app=leetcode.cn id=300 lang=cpp
 *
 * [300] 最长递增子序列
 */
#include<bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp;
        for (int num: nums) {
            int i = lower_bound(dp.begin(), dp.end(), num) - dp.begin();
            if (i >= int(dp.size())) {
                dp.emplace_back(num);
            } else {
                dp[i] = num;
            }
        }
        return dp.size();
    }
};
// @lc code=end

