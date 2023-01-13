/*
 * @lc app=leetcode.cn id=968 lang=cpp
 *
 * [968] 监控二叉树
 */
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int ans = 0;
    int dfs(TreeNode* node) {
        if (!node) return 1;
        int l = dfs(node->left);
        int r = dfs(node->right);
        if (l == 0 || r == 0) {
            ans += 1;
            return 2;
        } else if (l == 2 || r == 2) {
            return 1;
        } else {
            return 0;
        }
    }

public:
    int minCameraCover(TreeNode* root) {
        if (dfs(root) == 0) ans += 1;
        return ans;
    }
};
// @lc code=end

