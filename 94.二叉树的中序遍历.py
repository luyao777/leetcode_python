#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result

        def mid_search(root):
            if root.left:
                mid_search(root.left)
            result.append(root.val)
            if root.right:
                mid_search(root.right)

        mid_search(root)
        return result
        
# @lc code=end

