# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return True
        linked = []
        while(head):
            linked.append(head.val)
            head = head.next
        if(len(linked)%2 == 0):
            mid = len(linked)//2
            left, right = mid -1, mid
            while(left >= 0 and right < len(linked)):
                if(linked[left] != linked[right]):
                    return False
                left -= 1
                right += 1
            return True
        else:
            mid = len(linked)//2
            left, right = mid -1, mid + 1
            while(left >= 0 and right < len(linked)):
                if(linked[left] != linked[right]):
                    return False
                left -= 1
                right += 1
            return True
        return False
        
        # if head == None or head.next == None:
        #     return False
        # slow, fast, initial = head, head, head
        # prev = None
        # while(fast and fast.next):
        #     temp = slow 
        #     temp.next = prev
        #     prev = temp
        #     slow = slow.next
        #     fast = fast.next.next
        # while(slow):
        #     if(slow.val != initial.val):
        #         return False
        #     slow = slow.next
        #     intial = initial.next
        # return True