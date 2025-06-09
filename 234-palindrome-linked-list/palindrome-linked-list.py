# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        slow,fast=head,head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            Next=slow.next
            slow.next=prev
            prev=slow
            slow=Next
        if fast:
            slow=slow.next
        while slow and prev:
            if slow.val==prev.val:
                slow=slow.next
                prev=prev.next
            else:
                return False
        return True

            
        