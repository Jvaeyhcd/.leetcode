/*
 * @lc app=leetcode.cn id=124 lang=cpp
 *
 * [124] 二叉树中的最大路径和
 */
#include <bits/stdc++.h>
using namespace std;
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
public:
    int ans = INT_MIN;
    int dfs(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        int l = max(0, dfs(node->left));
        int r = max(0, dfs(node->right));
        ans = max(ans, l + r + node->val);
        return max(l, r) + node->val;
    }
    int maxPathSum(TreeNode* root) {
        dfs(root);
        return ans;
    }
};
// @lc code=end

