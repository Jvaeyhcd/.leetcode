/*
 * @lc app=leetcode.cn id=565 lang=swift
 *
 * [565] 数组嵌套
 */

// @lc code=start
class Solution {
    func arrayNesting(_ nums: [Int]) -> Int {
        let INF = 0xf3f3f3f3
        var ans = 0
        var arr = nums
        for i in 0..<arr.count {
            if arr[i] != INF {
                var start = arr[i]
                var count = 0
                while arr[start] != INF {
                    let tmp = start
                    start = arr[start]
                    count += 1
                    arr[tmp] = INF
                }
                ans = max(ans, count)
            }
        }
        return ans
    }
}
// @lc code=end

