# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        t = list()
        currNode = node
        while currNode != None:
            t.append(currNode)
            currNode = currNode.next

        m = len(t)
        for i in range(m - 1):
            t[i].val = t[i + 1].val

            if i == m - 2:
                t[i].next = None
