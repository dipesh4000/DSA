class Solution(object):
    @cache  # the memory trick can save some time
    def partition(self, s):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         res = []
#         part = []

#         def dfs(i):
#             if i >= len(s):
#                 res.append(part.copy())
#                 return
#             for j in range(i, len(s)):
#                 if self.isPal(s, i, j):
#                     part.append(s[i:j+1])
#                     dfs(j + 1)
#                     part.pop()
#         dfs(0)
#         return res
#     def isPal(self, s, l, r):
#         while l < r:
#             if s[1] != s[r]:
#                 return False
#             l, r = l + 1, r - 1
#         return True