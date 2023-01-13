/*
 * @lc app=leetcode.cn id=834 lang=cpp
 *
 * [834] 树中距离之和
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
    vector<int> ans;
    vector<int> cnts;
    vector<vector<int>> g;
    int n = 0;

    void sonDFS(int u, int pa) {
        for (int v: g[u]) {
            if (v == pa) continue;
            sonDFS(v, u);
            cnts[u] += cnts[v];
            ans[u] += ans[v] + cnts[v];
        }
    }

    void fatherDFS(int u, int pa) {
        for (int v: g[u]) {
            if (v == pa) continue;
            ans[v] = ans[u] - cnts[v] + n - cnts[v];
            fatherDFS(v, u);
        }
    }


public:
    vector<int> sumOfDistancesInTree(int N, vector<vector<int>>& edges) {
        n = N;
        g.resize(n);
        ans.resize(n);
        cnts.resize(n, 1);
        for (auto e: edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        sonDFS(0, -1);
        fatherDFS(0, -1);
        return ans;
    }
};
// @lc code=end

