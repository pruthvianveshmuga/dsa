# https://leetcode.com/problems/add-two-numbers/

import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution1(l1: ListNode, l2: ListNode):
    carry = 0
    ans = ListNode()
    curr = ans
    while l1 or l2 or carry:
        val = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
        carry, val = val//10, val%10
        curr.next = ListNode(val)
        curr, l1, l2 = curr.next, (l1.next if l1 else l1), (l2.next if l2 else l2)
    return ans.next
