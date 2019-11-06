'''
@Author: Yao Lu
@Date: 2019-11-05 20:18:00
@Description: 
'''
#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
                return True
        else:
            if self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.countDepth(0,root.left) - self.countDepth(0, root.right)) <= 1:
                return True
            else:
                return False
        
    def countDepth(self, cur_num, node):
        if node == None:
            return cur_num
        else:
            return max(self.countDepth(1+cur_num, node.left), self.countDepth(1+cur_num, node.right))
        
# @lc code=end

