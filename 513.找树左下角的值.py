#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def find_bottom_left_value(root, depth, tmp_value):
            if not root:
                return tmp_value, depth-1
            left_val, left_depth = find_bottom_left_value(root.left, depth+1, root.val)
            right_val, right_depth = find_bottom_left_value(root.right, depth+1, root.val)
            if left_depth >= right_depth:
                return left_val, left_depth
            else:
                return right_val, right_depth

        result, _ = find_bottom_left_value(root, 0, root.val)
        return result

        
# @lc code=end

