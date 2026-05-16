class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1

            elif nums[mid] < nums[r]:
                r = mid

            else:
                r -= 1

        return nums[l]
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         while len(nums) > 1 and nums[-1] == nums[0]:
#             nums.pop()
#         left, right = 0, len(nums) - 1
#         last = nums[right]
#         while (left < right):
#             mid = left + right >> 1

#             if (nums[mid] > last):
#                 left = mid + 1
#             else:
#                 right = mid
#         return nums[left]