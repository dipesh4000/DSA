class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # i = j = 0
        maxp = -inf
        negp = currp = 1
        neg = False
        for n in nums:
            currp *= n
            maxp = max(maxp, int(currp / negp), currp)
            if currp < 0 and not neg:
                negp = currp
                neg = True
            elif currp == 0:
                currp = negp = 1
                neg = False
        return maxp
