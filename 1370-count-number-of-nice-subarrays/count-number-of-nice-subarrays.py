class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pre = {0: 1}
        ans = 0
        summ = 0

        for i in nums:
            if i % 2 == 0:
                summ += 0
            else:
                summ += 1

            ans += pre.get(summ - k, 0)

            pre[summ] = pre.get(summ, 0) + 1

        return ans
