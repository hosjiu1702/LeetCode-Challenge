import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        nodesList = []
        nodesList.append(head)
        while nodesList[-1].next != None:
            nodesList.append(nodesList[-1].next)
        n = len(nodesList)
        middleNode = math.floor(n / 2)

        return nodesList[middleNode]