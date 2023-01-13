/*
 * @lc app=leetcode.cn id=2440 lang=cpp
 *
 * [2440] 创建价值相同的连通块
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int componentValue(vector<int>& nums, vector<vector<int>>& edges) {
        int n = nums.size(), target;
        vector<vector<int>> g(n);
        for (auto &e: edges) {
            int u = e[0], v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }
        function<int(int, int)> dfs = [&](int u, int pa) {
            int s = nums[u];
            for (int v: g[u]) {
                if (v == pa) continue;
                int res = dfs(v, u);
                if (res < 0) return -1;
                s += res;
            }
            if (s > target) return -1;
            return s < target ? s : 0;
        };

        int total = accumulate(nums.begin(), nums.end(), 0);
        int mx = *max_element(nums.begin(), nums.end());
        for (int i = min(n, total / mx);; --i) {
            if (total % i == 0) {
                target = total / i;
                if (dfs(0, -1) == 0) return i - 1;
            }
        }
        return 0;
    }
};
// @lc code=end

