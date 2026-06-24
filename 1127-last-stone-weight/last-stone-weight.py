class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -1 * heapq.heappop(maxHeap)
            x = -1 * heapq.heappop(maxHeap)
            if x != y:
                heapq.heappush(maxHeap, -1 * (y - x))

        if len(maxHeap) < 1:
            return 0
        return -1 * maxHeap[-1]


# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         for i in range(len(stones)):
#             stones[i] = -stones[i]
#         heapq.heapify(stones)
#         while len(stones) > 1:
#             largest = heapq.heappop(stones)
#             next_largest = heapq.heappop(stones)

#             if largest != next_largest:
#                 heapq.heappush(stones, largest - next_largest)

#         if len(stones) == 1:
#             return -heapq.heappop(stones)
#         return 0
