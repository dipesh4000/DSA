# class Solution:
#     def numSubseq(self, nums: List[int], target: int) -> int:
#         if not nums:
#             return 0
#         ans = 0
#         def subs(arr: List[int], index: int):
#             if(arr and index >= len(nums)):
#                 if(arr[0] + arr[-1]) <= target:
#                     ans += 1
#                 return
#             for i in range(index, len(nums)):
#                 if arr:
#                     subs(arr.append(nums[i]), index + 1)
#                 else:
#                     subs(arr, index + 1)
#         subs([], 0)
#         return ans
class Solution:
    def numSubseq(self, A, target):
        A.sort()
        l, r = 0, len(A) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if A[l] + A[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res % mod