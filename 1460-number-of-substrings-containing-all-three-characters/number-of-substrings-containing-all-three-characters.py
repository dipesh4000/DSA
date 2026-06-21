class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc = [0]*3
        i, j, count = 0, 0, 0
        while(j < len(s)):
            abc[ord(s[j]) - ord('a')] += 1
            while abc[0] > 0 and abc[1] > 0 and abc[2] > 0:
                count += len(s) - j
                abc[ord(s[i]) - ord('a')] -= 1
                i += 1
            j += 1
        return count