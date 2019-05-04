"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return []
        
        h = []
        h.append(head)

        stoppingFlag = False
        index = 0
        while not stoppingFlag:
            if h[index].next != None:
                h.append(h[index].next)
                index = index + 1
            else:
                stoppingFlag = True

        n = len(h)
        temp = [None for _ in range(n)]

        for i in range(n):
            temp[i] = h[n-1-i].val

        for i in range(n):
            h[i].val = temp[i]

        return head