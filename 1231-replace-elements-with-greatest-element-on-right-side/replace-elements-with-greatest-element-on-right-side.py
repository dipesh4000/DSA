# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         ans = [-1]*len(arr)
#         greatest_seen = -1
#         for i in range(len(arr) - 1, -1, -1):
#             ans[i] = greatest_seen
#             if(arr[i] > greatest_seen):
#                 greatest_seen = arr[i]
#         return ans


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        greatest_seen = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], greatest_seen = greatest_seen, max(greatest_seen, arr[i])

        return arr
