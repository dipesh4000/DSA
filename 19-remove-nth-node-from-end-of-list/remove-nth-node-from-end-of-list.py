# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        sz = self.getsize(head)
        if(sz == n):
            return head.next
        if(n > sz):
            return None
        point, future = head, head.next.next
        for i in range(sz - n - 1):
            point = point.next
            future = future.next
        point.next = future

        return head

    def getsize(self, head: Optional[ListNode]) -> int:
        size = 0
        while(head):
            size += 1
            head = head.next
        return size