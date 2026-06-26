# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Initial heads heap me daalo
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode()
        tail = dummy

        while heap:

            val, idx, node = heapq.heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return dummy.next
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         dummy = ListNode()
#         tail = dummy

#         while True:
#             min_val = float("inf")
#             min_node = None
#             min_index = -1

#             for i in range(0, len(lists)):
#                 if lists[i] and lists[i].val < min_val:
#                     min_val = lists[i].val
#                     min_node = lists[i]
#                     min_index = i

#             if min_node == None:
#                 break

#             tail.next = min_node
#             tail = tail.next

#             lists[min_index] = lists[min_index].next

#         tail.next = None
#         return dummy.next
# # curr[i] = head of every linked list

# # dummy = new ListNode()
# # tail = dummy

# # while(true):

# #     minNode = null
# #     minIndex = -1

# #     for i = 0 to k-1:
# #         if curr[i] != null:
# #             if minNode == null OR curr[i].val < minNode.val:
# #                 minNode = curr[i]
# #                 minIndex = i

# #     if minNode == null:
# #         break          // all lists exhausted

# #     tail.next = minNode
# #     tail = tail.next

# #     curr[minIndex] = curr[minIndex].next

# # tail.next = null
# # return dummy.next