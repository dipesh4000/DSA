class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)

        while low < high:
            mid = (low + high) // 2
            if self.rem(nums, mid, threshold):
                low = mid + 1
            else:
                high = mid
        return low

    def rem(self, nums: List[int], div: int, threshold: int) -> bool:
        # sum(math.ceil(x / div) for x in arr)
        return sum(math.ceil(x / div) for x in nums) > threshold