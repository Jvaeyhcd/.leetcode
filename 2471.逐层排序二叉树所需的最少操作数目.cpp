/*
 * @lc app=leetcode.cn id=2471 lang=cpp
 *
 * [2471] 逐层排序二叉树所需的最少操作数目
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
 * /**
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
    int minimumOperations(TreeNode* root) {
        vector<vector<int>> arr;
        deque<TreeNode *> q;
        q.push_back(root);
        while (!q.empty()) {
            vector<int> a;
            for (int i = 0; i < q.size(); i++) {
                TreeNode *u = q.front();
                q.pop_front();
                a.push_back(u->val);
                // cout << u->val << " ";
                if (u->left != nullptr) q.push_back(u->left);
                if (u->right != nullptr) q.push_back(u->right);
            }
            // cout << endl;
            arr.push_back(a);
        }

        int ans = 0;

        function<int(vector<int>&)> helper = [](vector<int>& nums) -> int {
            int n = nums.size();
            vector<int> arr = nums;
            sort(arr.begin(), arr.end());
            unordered_map<int, int> mp;
            for (int i = 0; i < n; i++) {
                mp[arr[i]] = i;
            }
            vector<bool> flags(n, false);
            int loop = 0;

            for (int i = 0; i < n; i++) {
                if (flags[i]) continue;
                int j = i;
                while (!flags[j]) {
                    flags[j] = true;
                    j = mp[nums[j]];
                }
                loop += 1;
            }
            return n - loop;
        };

        for (auto &a: arr) {
            ans += helper(a);
        }

        return ans;
    }
};
// @lc code=end

