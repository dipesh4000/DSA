# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            
            nxt = slow.next      
            slow.next = prev     
            prev = slow
            slow = nxt
        if fast:
            slow = slow.next
        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        
        return True
        # if head == None or head.next == None:
        #     return True
        # linked = []
        # while(head):
        #     linked.append(head.val)
        #     head = head.next
        # if(len(linked)%2 == 0):
        #     mid = len(linked)//2
        #     left, right = mid -1, mid
        #     while(left >= 0 and right < len(linked)):
        #         if(linked[left] != linked[right]):
        #             return False
        #         left -= 1
        #         right += 1
        #     return True
        # else:
        #     mid = len(linked)//2
        #     left, right = mid -1, mid + 1
        #     while(left >= 0 and right < len(linked)):
        #         if(linked[left] != linked[right]):
        #             return False
        #         left -= 1
        #         right += 1
        #     return True
        # return False