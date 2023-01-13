/*
 * @lc app=leetcode.cn id=927 lang=cpp
 *
 * [927] 三等分
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:

    int find(vector<int>& arr, int x) {
        int s = 0;
        for (int i = 0; i < arr.size(); i++) {
            s += arr[i];
            if (s == x) {
                return i;
            }
        }
        return 0;
    }

    vector<int> threeEqualParts(vector<int>& arr) {
        int n = arr.size();
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += arr[i];
        }
        int cnt = sum / 3, mod = sum % 3;
        if (mod > 0) {
            return {-1, -1};
        }
        if (cnt == 0) {
            return {0, n - 1};
        }
        int i = find(arr, 1), j = find(arr, cnt + 1), k = find(arr, cnt << 1 | 1);
        while (k < n && arr[i] == arr[j] && arr[j] == arr[k]) {
            i += 1;
            j += 1;
            k += 1;
        }
        if (k == n) {
            return {i - 1, j};
        } else {
            return {-1, -1};
        }
    }
};
// @lc code=end

