class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1

        for i in range(0, len(nums)):
            if(nums[i] == 0):
                j = i
                break
        
        for i in range(j, len(nums)):
            if(nums[i] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                j += 1