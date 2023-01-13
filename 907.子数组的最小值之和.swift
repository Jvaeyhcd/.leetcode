/*
 * @lc app=leetcode.cn id=907 lang=swift
 *
 * [907] 子数组的最小值之和
 */

// @lc code=start
class Solution {
    func sumSubarrayMins(_ arr: [Int]) -> Int {
        let MOD = 1_000_000_007
        var ans = 0
        let n = arr.count

        var stack = [Int]()
        var left = [Int](repeating: -1, count: n)
        for i in 0..<n {
            while stack.count > 0 && arr[i] <= arr[stack[stack.count - 1]] {
                stack.removeLast()
            }
            if stack.count > 0 {
                left[i] = stack[stack.count - 1]
            }
            stack.append(i)
        }

        stack.removeAll()
        var right = [Int](repeating: n, count: n)
        var i = n - 1
        while i >= 0 {
            while stack.count > 0 && arr[i] < arr[stack[stack.count - 1]] {
                stack.removeLast()
            }
            if stack.count > 0 {
                right[i] = stack[stack.count - 1]
            }
            stack.append(i)
            i -= 1
        }

        for i in 0..<n {
            ans += (i - left[i]) * (right[i] - i) * arr[i]
        }
        
        return ans % MOD
    }
}
// @lc code=end

