'''
@Author: Yao Lu
@Date: 2019-11-06 12:40:03
@Description: 
'''
#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return self.countDepth(0,root)
    def countDepth(self, cur_num, node):
        if node == None:
            return cur_num
        else:
            if node.left == None and node.right == None:
                return cur_num + 1
            elif node.left == None:
                return self.countDepth(1+cur_num, node.right)
            elif node.right == None:
                return self.countDepth(1+cur_num, node.left)
            else:
                return min(self.countDepth(1+cur_num, node.left), self.countDepth(1+cur_num, node.right))
        
# @lc code=end

