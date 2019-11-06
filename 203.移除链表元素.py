'''
@Author: Yao Lu
@Date: 2019-11-06 20:30:42
@Description: 
'''
#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        while(head!= None and head.val == val):
            head = head.next
        p = head
        while(p!= None and p.next != None):
            if p.next.val == val:
                p.next = p.next.next 
            else:
                p = p.next
        return head
        
# @lc code=end
