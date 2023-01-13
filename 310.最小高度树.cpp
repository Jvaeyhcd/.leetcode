/*
 * @lc app=leetcode.cn id=310 lang=cpp
 *
 * [310] 最小高度树
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
    vector<vector<int>> g;
    // height0表示子树高，height表示树高
    vector<int> height0, height;

    // 计算以0号节点为根的树中，以各个节点为根的子树高
    void dfs1(int u) {
        height0[u] = 1;
        int h = 0;
        for (int v: g[u]) {
            if (height0[v] != 0) continue;
            dfs1(v);
            h = max(h, height0[v]);
        }
        height0[u] = h + 1;
    }

    // 进行换根动态规划，计算出所有的树高
    void dfs2(int u) {
        // 计算子树高的最大值和次大值
        int first = 0, second = 0;
        for (int v: g[u]) {
            if (height0[v] > first) {
                second = first;
                first = height0[v];
            } else if (height0[v] > second){
                second = height0[v];
            }
        }
        for (int v: g[u]) {
            // 树高已计算出，跳过这个节点
            if (height[v] != 0) continue;
            // 更新以当前节点为根的子树高，换根到v
            height0[u] = (height0[v] != first ? first : second) + 1;
            height[v] = max(height0[v], height0[u] + 1);
            // 递归进行换根动态规划
            dfs2(v);
        }
    }

public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        g.resize(n);
        height0.resize(n, 0);
        height.resize(n, 0);
        for (auto& e: edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        dfs1(0);
        dfs2(0);
        vector<int> ans;
        int h = n;
        for (int i = 0; i < n; i++) {
            if (height[i] < h) {
                h = height[i];
                ans.clear();
            }
            if (height[i] == h) ans.push_back(i);
        }
        return ans;
    }
};
// @lc code=end

