class Solution:
    def arrayRankTransform(self, arr):
        rank = {}

        for i, num in enumerate(sorted(set(arr)), 1):
            rank[num] = i

        return [rank[num] for num in arr]
# class Solution:
#     def arrayRankTransform(self, arr):
#         nums = sorted(arr)

#         rank = {}
#         current = 1

#         for num in nums:
#             if num not in rank:
#                 rank[num] = current
#                 current += 1

#         return [rank[num] for num in arr]
