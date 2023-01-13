/*
 * @lc app=leetcode.cn id=988 lang=cpp
 *
 * [988] 从叶结点开始的最小字符串
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
    string ans = "~";
    string smallestFromLeaf(TreeNode* root) {

        function<void(TreeNode*, vector<char>&)> dfs = [&](TreeNode* node, vector<char>& path) {
            if (node == nullptr) return;
            path.push_back('a' + node->val);
            if (node->left == nullptr && node->right == nullptr) {
                string str(path.begin(), path.end());
                reverse(str.begin(), str.end());
                if (str < ans) ans = str;
            }
            dfs(node->left, path);
            dfs(node->right, path);
            path.pop_back();
        };
        vector<char> path;
        dfs(root, path);
        return ans;
    }
};
// @lc code=end

