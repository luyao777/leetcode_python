#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root, p, q):
            if not root:
                return False
            if root.val == p.val or root.val == q.val:
                return True
            left_flag, right_flag = False, False
            if find(root.left, p, q):
                left_flag = True
            else:
                root.left = None
            if find(root.right, p, q):
                right_flag = True
            else:
                root.right = None

            if right_flag or left_flag:
                return True
            else:
                return False

        find(root, p, q)
        while(not(root.val == p.val or root.val == q.val or (root.right and root.left))):
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
        return root

# @lc code=end

