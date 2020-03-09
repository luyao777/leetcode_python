#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        node_id = 0
        head_pre = head
        big_node = None
        ans = head.next
        while (head.next):
            head = head.next
            node_id += 1
            if node_id % 2 == 1:
                head_pre.next = head.next
                if big_node is not None:
                    big_node.next = head
                head.next = head_pre        
                head = head.next
                big_node = head
            head_pre = head
        return ans


# @lc code=end
