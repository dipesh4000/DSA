class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 1 and nums[-1] == nums[0]:
            nums.pop()
        left, right = 0, len(nums) - 1
        last = nums[right]
        while (left < right):
            mid = left + right >> 1

            if (nums[mid] > last):
                left = mid + 1
            else:
                right = mid
        return nums[left]