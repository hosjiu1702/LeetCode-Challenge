# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        retList = []
        
        if l1 != None:
            retList.append(l1)
            while retList[-1].next != None:
                retList.append(retList[-1].next)
            if l2 != None:
                retList[-1].next = l2
                while retList[-1].next != None:
                    retList.append(retList[-1].next)
        else:
            if l2 != None:
                retList.append(l2)
                while retList[-1].next != None:
                    retList.append(retList[-1].next)  
            else:
                return l1

        
        temp = []
        for i in range(len(retList)):
            temp.append(retList[i].val)
        
        temp.sort()
        
        for i in range(len(retList)):
            retList[i].val = temp[i]

        return retList[0]