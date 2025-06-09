# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        summ=0
        slow,fast=head,head
        prev=None
        # while fast and fast.next:
        #     prev=slow
        #     slow=slow.next
        #     fast=fast.next.next
        # prev.next=None
        # prev=None
        # while slow:
        #     fast=slow.next
        #     slow.next=prev
        #     prev=slow
        #     slow=fast
        # while head and prev:
        #     x=prev.val+head.val
        #     summ=max(x,summ)
        #     head,prev=head.next,prev.next
        # return summ
        while fast and fast.next:
            fast=fast.next.next
            Next=slow.next
            slow.next=prev
            prev=slow
            slow=Next
        while slow and prev:
            summ=max(summ,prev.val+slow.val)
            slow,prev=slow.next,prev.next
        return summ


        
            
        