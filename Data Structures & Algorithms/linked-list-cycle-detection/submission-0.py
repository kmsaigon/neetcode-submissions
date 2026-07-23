# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        curr = head
        seen = {}

        while curr:
            if curr not in seen:
                seen[curr] = curr.val
                curr = curr.next
                continue
            
            return True
        
        return False