# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt=0
        cur=head
        while cur:
            cnt+=1
            cur=cur.next
        
        if cnt-n == 0:
            head = head.next
        else:
            count = 0
            node1 = head
            while count < cnt-n-1 and node1:
                count += 1
                node1 = node1.next
            if node1 and node1.next:
                node1.next = node1.next.next
        return head
