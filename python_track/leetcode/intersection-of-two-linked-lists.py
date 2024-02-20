# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited={}
        

        dummyA = ListNode(0)
        dummyA.next = headA
        dummyB = ListNode(0)
        dummyB.next = headB
        cur=dummyA
        while cur:
            visited[cur.next]=0
            cur=cur.next
        
        curr=dummyB
        while curr:
            if curr.next in visited:
                return curr.next
            curr=curr.next
        return None
