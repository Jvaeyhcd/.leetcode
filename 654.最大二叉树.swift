/*
 * @lc app=leetcode.cn id=654 lang=swift
 *
 * [654] 最大二叉树
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func constructMaximumBinaryTree(_ nums: [Int]) -> TreeNode? {
        return self.construct(nums, 0, nums.count)
    }

    func construct(_ nums: [Int], _ l: Int, _ r: Int) -> TreeNode? {
        if l == r {
            return nil
        }
        let max_i = self.max(nums, l, r)
        var root = TreeNode(nums[max_i])
        root.left = self.construct(nums, l, max_i)
        root.right = self.construct(nums, max_i + 1, r)
        return root
    }

    func max(_ nums: [Int], _ l: Int, _ r: Int) -> Int {
        var max_i = l
        var i = l
        while i < r {
            if nums[i] > nums[max_i] {
                max_i = i
            }
            i += 1
        }
        return max_i
    }
}
// @lc code=end

