# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
    
        part_size = length // k
        remainder = length % k

       
        curr = head
        result = []

       
        for i in range(k):
            part_head = curr
           
            part_length = part_size + 1 if i < remainder else part_size

            for j in range(part_length - 1):
                if curr:
                    curr = curr.next

          
            if curr:
                next_node = curr.next
                curr.next = None
                curr = next_node

            result.append(part_head)

        return result