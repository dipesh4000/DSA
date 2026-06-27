class Solution:
    def arrayRankTransform(self, arr):
        nums = sorted(arr)

        rank = {}
        current = 1

        for num in nums:
            if num not in rank:
                rank[num] = current
                current += 1

        return [rank[num] for num in arr]
