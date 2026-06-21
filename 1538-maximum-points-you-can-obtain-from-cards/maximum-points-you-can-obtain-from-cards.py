class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        if k == n:
            return sum(cardPoints)

        window = n - k

        curr = sum(cardPoints[:window])
        min_window = curr

        for r in range(window, n):
            curr += cardPoints[r]
            curr -= cardPoints[r - window]
            min_window = min(min_window, curr)

        return sum(cardPoints) - min_window