/*
 * @lc app=leetcode.cn id=670 lang=swift
 *
 * [670] 最大交换
 */

// @lc code=start
class Solution {
    func maximumSwap(_ num: Int) -> Int {
        var arr = [Int]()
        var a = num
        while a > 0 {
            arr.append(a % 10)
            a /= 10
        }
        arr.reverse()
        var right = [Int](repeating: arr.count - 1, count: arr.count)
        let range = 0..<arr.count
        
        var stack = [Int]()
        for i in range.reversed() {
            while !stack.isEmpty && arr[stack.count - 1] > arr[i] {
                stack.removeLast()
            }
            print(i, stack)
            if !stack.isEmpty {
                right[i] = stack[stack.count - 1]
            }

            stack.append(i)
        }
        print(right)

        var ans = 0
        return ans
    }
}
// @lc code=end

var solution = Solution()
var num = 2736
num = 9973
num = 983698
print(solution.maximumSwap(num))