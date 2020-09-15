#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        r_node = lists.pop(0)
        tmp_r_node = r_node
        for i in range(1, len(lists)):
            c_node = lists[i]
            while(c_node):
                if r_node.val < c_node.val and r_node.next.val

        
# @lc code=end

