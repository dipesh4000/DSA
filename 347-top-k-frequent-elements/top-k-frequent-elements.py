from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        heap = []
        
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
                
        return [num for count, num in heap]

# from collections import Counter


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = Counter(nums)
#         return [num for num, count in freq.most_common(k)]
