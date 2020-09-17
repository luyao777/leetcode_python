#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        fa_queue = [root]
        ch_queue = []
        tmp_result = []
        while(fa_queue):
            node = fa_queue.pop(0)
            if node.left: ch_queue.append(node.left)
            if node.right: ch_queue.append(node.right)
            tmp_result.append(node.val)
            if not fa_queue:
                result.append(tmp_result)
                fa_queue = ch_queue
                ch_queue = []
                tmp_result = []
        return result

# @lc code=end

