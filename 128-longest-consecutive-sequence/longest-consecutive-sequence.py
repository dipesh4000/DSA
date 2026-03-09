class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        size = 1
        maxsize = 1
        for i in range(1, len(nums)):
            if(nums[i] == (nums[i - 1] + 1)):
                size += 1
            else:
                size = 1
            maxsize = max(maxsize, size)
        return maxsize