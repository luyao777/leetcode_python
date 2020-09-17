#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = []
        if not root:
            return True

        def mid_search(root):
            if root.left:
                mid_search(root.left)
            result.append(root.val)
            if root.right:
                mid_search(root.right)

        mid_search(root)
        print(result)
        for i in range(1, len(result)):
            if result[i] <= result[i-1]:
                return False
        return True
# @lc code=end

