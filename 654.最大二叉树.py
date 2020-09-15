#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        max_num = -float('inf')
        max_node_i = -1
        for i in range(len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
                max_node_i = i
        root = TreeNode(nums[max_node_i])
        root.left = self.constructMaximumBinaryTree(nums[:max_node_i])
        root.right = self.constructMaximumBinaryTree(nums[max_node_i+1:])

        return root

        
# @lc code=end

