#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        fa_queue = [root]
        ch_queue = []
        tmp_result = []
        i = 1
        while(fa_queue):
            node = fa_queue.pop(0)
            if node.right: ch_queue.append(node.right)
            if node.left: ch_queue.append(node.left)
            tmp_result.append(node.val)
            if not fa_queue:
                if i % 2 == 1:
                    tmp_result = tmp_result[::-1]
                i += 1
                result.append(tmp_result)
                fa_queue = ch_queue
                ch_queue = []
                tmp_result = []
        return result
# @lc code=end

