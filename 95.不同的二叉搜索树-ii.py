#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        dct = {}

        def left_right(left: int, right: int) -> List[TreeNode]:
            if left > right:
                return [None]
            if (left, right) in dct:
                return dct[(left, right)]
            ret = []
            for i in range(left, right+1):
                left_lst = left_right(left, i-1)
                right_lst = left_right(i+1, right)
                for L in left_lst:
                    for R in right_lst:
                        app_Tree = TreeNode(i)
                        app_Tree.left = L
                        app_Tree.right = R
                        ret.append(app_Tree)
            dct[(left, right)] = ret
            return ret

        return left_right(1, n)
        
# @lc code=end

