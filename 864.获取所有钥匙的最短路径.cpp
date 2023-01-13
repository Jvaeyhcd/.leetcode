/*
 * @lc app=leetcode.cn id=864 lang=cpp
 *
 * [864] 获取所有钥匙的最短路径
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    using node = tuple<int, int, int>;
    int shortestPathAllKeys(vector<string>& grid) {
        int m = grid.size(), n = grid[0].size();
        int keyCnt = 0;
        vector<vector<vector<bool>>> vis(m, vector<vector<bool>>(n, vector<bool>(1 << keyCnt)));
        deque<tuple<int, int, int, int>> q;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '@') {
                    q.push_back(tuple(i, j, 0, 0));
                    vis[i][j][0] = true;
                } else if (islower(grid[i][j])) {
                    keyCnt += 1;
                }
            }
        }

        int dirs[5] = {1, 0, -1, 0, 1};

        while (!q.empty()) {
            int x, y, step, status;
            tie(x, y, step, status) = q.front();
            q.pop_front();
            int cnt = 0;
            for (int i = 0; i < 6; i++) {
                if ((status >> i) & 1) {
                    cnt += 1;
                }
            }
            if (cnt == keyCnt) {
                return step;
            }
            cout << x << " " << y << endl;

            for (int i = 0; i < 4; i++) {
                int nx = x + dirs[i];
                int ny = y + dirs[i + 1];
                if (!(0 <= nx && nx < m && 0 <= ny && ny < n) || vis[nx][ny][status]) {
                    continue;
                }

                if (grid[nx][ny] == '#') {
                    continue;
                } else if (islower(grid[nx][ny])) {
                    cout << grid[nx][ny] << (1 << (grid[nx][ny] - 'a')) << endl;
                    vis[nx][ny][status | (1 << (grid[nx][ny] - 'a'))] = true;
                    q.push_back(make_tuple(nx, ny, step + 1, status | (1 << (grid[nx][ny] - 'a'))));
                    continue;
                } else if (isupper(grid[nx][ny]) && ((1 << (grid[nx][ny] - 'A')) & status) == 0) {
                    continue;
                }

                vis[nx][ny][status] = true;
                q.push_back(make_tuple(nx, ny, step + 1, status));
            }

        }

        return -1;
    }
};
// @lc code=end

