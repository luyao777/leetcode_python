#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        # 就是说找到节点之后 在把左右子树放到正确的位置上去

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            # 就是找到当前节点了 看他的左子树 还是右子树
            left = root.left
            right = root.right
            if not left:
                # 左子树为空
                return root.right
            elif not right:
                # 右子树为空
                return root.left
            else:
                # 左右子树都不为空 可以找到右子树的最左节点
                # 这是用来给上一级返回的
                r = right
                while right.left:
                    right = right.left
                right.left = left
                return r

# @lc code=end

