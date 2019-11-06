'''
@Author: Yao Lu
@Date: 2019-11-06 14:31:41
@Description: 
'''
#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if head.val == 'Yao Lu':
                return True
            else:
                head.val = 'Yao Lu'
            head = head.next
        return False
        
# @lc code=end

