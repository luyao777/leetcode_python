'''
@Author: Yao Lu
@Date: 2019-11-07 16:18:31
@Description: 
'''
#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        node_list = []
        while(head != None):
            node_list.insert(0,head)
            head = head.next
        for index, node in enumerate(node_list):
            if index == len(node_list)-1:
                node.next = None
                break
            node.next = node_list[index+1]
        return node_list[0]
        





        
# @lc code=end

