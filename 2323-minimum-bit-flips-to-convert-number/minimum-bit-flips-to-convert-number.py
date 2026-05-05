class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num = start^goal
        result = bin(num).count('1')
        return result