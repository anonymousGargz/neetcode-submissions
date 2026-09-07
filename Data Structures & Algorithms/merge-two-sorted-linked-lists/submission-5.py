# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1):
            return list2
        if (not list2):
            return list1
        newHead=None
        counter=ListNode()
        counter.next=newHead
        if (list1.val<= list2.val):
            newHead=ListNode(list1.val)
            list1=list1.next
        else:
            newHead=ListNode(list2.val)
            list2=list2.next
        counter=ListNode()
        counter.next=newHead
        while list1 and list2:
            if (list1.val<=list2.val):
                newHead.next=ListNode(list1.val)
                list1=list1.next
            else:

                newHead.next=ListNode(list2.val)
                list2=list2.next
            newHead=newHead.next
        while list1:
            newHead.next=ListNode(list1.val)
            list1=list1.next
            newHead=newHead.next
        while list2:
            newHead.next=ListNode(list2.val)
            list2=list2.next
            newHead=newHead.next
        counter=counter.next
        return (counter)
        
            



        