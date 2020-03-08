#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def node_path(root, s):
            if root:
                s += str(root.val)
                if not root.left and not root.right:
                    path.append(s)
                else:
                    s += '->'
                    node_path(root.left, s)
                    node_path(root.right, s)

        path = []
        node_path(root, '')
        return path
        
# @lc code=end

