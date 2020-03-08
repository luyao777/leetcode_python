#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pali = None
        ori_head = head
        list_len = 0

        while(head is not None):
            pali_head = ListNode(head.val)
            pali_head.next = pali
            head = head.next
            pali = pali_head
            list_len += 1

        for i in range(list_len):
            if pali.val != ori_head.val:
                return False
            pali = pali.next
            ori_head = ori_head.next

        return True

# @lc code=end

