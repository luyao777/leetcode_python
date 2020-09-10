#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxsum = float('-inf')
        def dfs(r):
            if not r: return 0
            left = dfs(r.left)
            right = dfs(r.right)
            self.maxsum = max(self.maxsum, left + right + r.val)
            return max(0, max(left, right) + r.val)
        dfs(root)
        return self.maxsum
# @lc code=end
