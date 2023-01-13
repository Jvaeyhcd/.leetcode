/*
 * @lc app=leetcode.cn id=813 lang=cpp
 *
 * [813] 最大平均值和的分组
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    double largestSumOfAverages(vector<int>& nums, int K) {
        int n = nums.size(), presum[n + 1];
        memset(presum, 0, sizeof(presum));
        vector<vector<double>> dp(n, vector<double>(K + 1, 0.0));

        for (int i = 0; i < n; i++) {
            presum[i + 1] = presum[i] + nums[i];
            dp[i][1] = presum[i + 1] * 1.0 / (i + 1);
        }
        for (int k = 2; k <= K; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = k - 2; j < i; j++) {
                    dp[i][k] = max(dp[i][k], dp[j][k - 1] + (presum[i + 1] - presum[j + 1]) * 1.0 / (i - j));
                }
            }
        }

        return dp[n - 1][K];
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution solution = Solution();
    vector<int> nums = {1,2,3,4,5,6,7};
    int k = 4;
    cout << solution.largestSumOfAverages(nums, k) << endl;
    return 0;
}
