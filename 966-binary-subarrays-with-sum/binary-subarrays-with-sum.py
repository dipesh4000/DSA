class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre={0:1}
        ans=0
        summ=0

        for i in nums:
            summ+=i

            ans+=pre.get(summ-goal, 0)

            pre[summ]=pre.get(summ, 0)+1

        return ans
# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         def helper(x):
#             if x < 0: return 0
#             res = 0
#             l, cur = 0, 0
#             for r in range(len(nums)):
#                 cur += nums[r]
#                 while cur > x:
#                     cur -= nums[l]
#                     l += 1
#                 res += (r-l + 1)
#             return res
#         return helper(goal) - helper(goal -1)