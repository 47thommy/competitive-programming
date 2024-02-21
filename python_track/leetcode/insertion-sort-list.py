# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        arr = []
        while tmp :
            arr.append(tmp.val)
            tmp = tmp.next
        arr.sort()
        dummy = ListNode(0)
        l = dummy
        for i in range(len(arr)):
            l.next = ListNode(arr[i])
            l = l.next
        return dummy.next
        