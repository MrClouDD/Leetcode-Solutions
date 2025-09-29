#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
# from custom_library.ListNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carry = 0
        
        while l1 or l2 or carry:
    
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry

            curr.next = ListNode(total % 10)
            curr = curr.next
            
            carry = total // 10
                
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        
        return head.next
            
# @lc code=end

