/*
 * @lc app=leetcode.cn id=826 lang=cpp
 *
 * [826] 安排工作以达到最大收益
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        int n = difficulty.size();
        vector<pair<int, int>> jobs(n);

        for (int i = 0; i < n; ++i) {
            jobs[i] = make_pair(difficulty[i], profit[i]);
        }
        sort(jobs.begin(), jobs.end());
        sort(worker.begin(), worker.end());
        int ans = 0;
        int best = 0;
        int idx = 0;
        for (int w: worker) {
            while (idx < n && w >= jobs[idx].first) {
                best = max(best, jobs[idx++].second);
            }
            ans += best;
        }
        return ans;
    }
};
// @lc code=end

