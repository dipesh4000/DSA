class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        while(l<r):
            mid = (l + r)//2

            if(self.isgreater(nums, k, mid)):
                l = mid + 1
            else:
                r = mid
        return l
    def isgreater(self, nums: List[int], k: int, mid: int) -> bool:
        maxsum = 0
        subcount = 1

        for num in nums:
            if(subcount < k):
                maxsum += num
                if(maxsum > mid):
                    maxsum = num
                    subcount += 1
            else:
                maxsum += num
        return maxsum > mid