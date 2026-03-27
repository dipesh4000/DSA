class Solution:
    def maxDepth(self, s: str) -> int:
        d = ans = 0
        for c in s:
            d += (c == '(') - (c == ')')
            ans = max(ans, d)
        return ans



# class Solution:
#     def maxDepth(self, s: str) -> int:
#         depth = 0
#         mdepth = 0
#         for ch in s:
#             if(ch == "("):
#                 depth += 1
#                 mdepth = max(mdepth, depth)
            
#             if(ch == ")"):
#                 depth -= 1
#         return mdepth
