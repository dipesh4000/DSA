import math

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648   # -2^31
        MAX = 2147483647    # 2^31 - 1

        res = 0

        while x:
            # Get last digit (handles negatives properly)
            digit = int(math.fmod(x, 10))

            # Remove last digit
            x = int(x / 10)

            # Check overflow before multiplying
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0

            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0

            res = res * 10 + digit

        return res
# class Solution:
#     def reverse(self, x: int) -> int:
#         sign = -1 if x < 0 else 1
#         x = abs(x)
        
#         rev = 0
        
#         while x:
#             digit = x % 10
#             rev = rev * 10 + digit
#             x //= 10
        
#         rev *= sign
        
#         if rev < -2**31 or rev > 2**31 - 1:
#             return 0
        
#         return rev