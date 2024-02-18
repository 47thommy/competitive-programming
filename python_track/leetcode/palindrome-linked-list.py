# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse_linked_list(head):
            prev,current=None,head
            while current:
                next=current.next
                current.next=prev
                prev=current
                current=next
            return prev
        
        real=[]
        current=head
        while current:
            real.append(current.val)
            current=current.next
        reverse=[]

        cur=reverse_linked_list(head)
        while cur:
            reverse.append(cur.val)
            cur=cur.next
        print(real)
        print(reverse)

        
        return (real==reverse)