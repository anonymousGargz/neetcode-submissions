# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        myHeap = []

        for linkedList in lists:
            while linkedList:
                heapq.heappush(myHeap, linkedList.val)
                linkedList = linkedList.next

        if not myHeap:
            return None

        newHead = ListNode(heapq.heappop(myHeap))
        pointer = newHead

        while myHeap:
            newHead.next = ListNode(heapq.heappop(myHeap))
            newHead = newHead.next

        return pointer
