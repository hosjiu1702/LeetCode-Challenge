# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # Using Two-Pointer algorithm (address-based)
        """
        if head == None:
            return False

        currNode = head
        if currNode.next != None:
            nextNode = currNode.next
        else:
            return False

        while currNode < nextNode:
            currNode = nextNode
            if currNode.next != None:
                nextNode = currNode.next
            else:
                return False

        return True
        """

        # Using hash table algorithm
        t = dict()

        if head == None:
            return False
        else:
            currNode = head
            t[currNode] = id(currNode)

        while currNode.next != None:
            currNode = currNode.next
            
            if currNode in t:
                return True
            
            t[currNode] = id(currNode)


        return False