# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head != None:
            listNode = []

            listNode.append(head)
            while listNode[-1].next != None:
                listNode.append(listNode[-1].next)

            indexList = []
            for i in range(len(listNode) - 1):
                if listNode[i].val == listNode[i + 1].val:
                    indexList.append(i+1)
            
            temp = []
            for i in range(len(listNode)):
                if len(indexList) != 0:
                    if i != indexList[0]:
                        temp.append(listNode[i])
                    else:
                        indexList.pop(0)
                else:
                    temp.append(listNode[i])

            currIndex = 0
            while currIndex < len(temp) - 1:
                temp[currIndex].next = temp[currIndex + 1]
                currIndex += 1

            if temp[-1].next != None:
                temp[-1].next = None

        return head