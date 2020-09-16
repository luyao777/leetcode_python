#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.node_val = []

        def read_tree(node):
            if not node:
                return
            if node.left:
                read_tree(node.left)
            self.node_val.append(node.val)
            if node.right:
                read_tree(node.right)
        read_tree(root)


    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.node_val.pop(0)



    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.node_val) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

