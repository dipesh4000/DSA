class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
    
        if n % 2 == 0:
            half = self.myPow(x, n//2)
            return half * half        # reuse, don't call twice!
        else:
            return x * self.myPow(x, n-1)
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         def helper(x, n):
#             if x == 0: return 0
#             if n == 0: return 1

#             res = helper(x*x, n//2)
#             return x*res if n % 2 else res
#         res = helper(x, abs(n))
#         return res if n>=0 else 1/res