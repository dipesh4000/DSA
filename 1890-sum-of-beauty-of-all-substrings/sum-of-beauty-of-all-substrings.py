from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                freq = Counter(sub).values()
                ans += max(freq) - min(freq)
                
        return ans