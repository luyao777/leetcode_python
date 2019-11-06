'''
@Author: Yao Lu
@Date: 2019-11-06 13:12:14
@Description: 
'''
#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.sumValue(0, root, sum)

    def sumValue(self, cur_value, root, sum):
        if root == None:
            return False
        else:
            cur_value += root.val
            if root.left == None and root.right == None:
                if cur_value == sum:
                    return True
                else:
                    return False
            return self.sumValue(cur_value,root.left, sum) or self.sumValue(cur_value,root.right, sum)
        
# @lc code=end

