class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(openN: int, closeN: int, s: str):
            if(openN == closeN == n):
                ans.append(s)
                return
            
            if(closeN < openN):
                backtrack(openN,closeN + 1, s + ")")
            if(openN < n):
                backtrack(openN + 1,closeN, s + "(")
        backtrack(0, 0, "")
        return ans