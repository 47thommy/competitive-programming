class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                fast = head 

                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                
                return slow
        
        return None