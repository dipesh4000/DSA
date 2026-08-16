class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gr = si = 0
        ans = 0
        while gr < len(g) and si < len(s):
            if g[gr] <= s[si]:
                ans += 1
                gr += 1
                si += 1
            else:
                si += 1
        return ans
