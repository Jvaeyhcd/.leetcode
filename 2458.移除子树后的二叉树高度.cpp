/*
 * @lc app=leetcode.cn id=2458 lang=cpp
 *
 * [2458] 移除子树后的二叉树高度
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
public:
    vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
        unordered_map<TreeNode *, int> height;
        function<int(TreeNode *)> getHeight = [&](TreeNode* node) -> int {
            return node ? height[node] = 1 + max(getHeight(node->left), getHeight(node->right)) : 0;
        };
        getHeight(root);

        int res[height.size() + 1];
        function<void(TreeNode*, int, int)> dfs = [&](TreeNode* node, int depth, int restH) {
            if (node == nullptr) return;
            depth += 1;
            res[node->val] = restH;
            dfs(node->left, depth, max(restH, depth + height[node->right]));
            dfs(node->right, depth, max(restH, depth + height[node->left]));
        };

        dfs(root, -1, 0);
        for (auto &q: queries) q = res[q];
        return queries;
    }
};
// @lc code=end

