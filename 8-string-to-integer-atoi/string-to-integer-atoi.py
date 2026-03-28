class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        i = 0
        sign = 1

        # sign
        if s[0] in '+-':
            sign = -1 if s[0] == '-' else 1
            i += 1

        num = 0

        # digits
        while i < len(s) and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num



# class Solution:
#     def myAtoi(self, s: str) -> int:
#         #eleminating leading whitespaces
#         s = s.strip()
#         if not s:
#             return 0
#         #doing negative check
#         neg = 1
#         if(s[0] in ['-', '+']):
#             if(s[0] == "-"):
#                 neg *= (-1)
#             s = s[1:]
#         if not s:
#             return 0
#         #removed leading zeroes
#         s = self.removeleadingzero(s)

#         if not s:
#             return 0
#         #readinglines
#         ans = ""
#         for i in s:
#             if(i.isdigit()):
#                 ans += i
#             else:
#                 break
#         if not ans:
#             return 0

#         #performing roundoffs
#         if(int(ans) > 2147483647 and neg == -1):
#             return -2147483648
#         if(int(ans) > 2147483647):
#             return 2147483647
#         if(neg == -1):
#             return int(ans)*(-1)
#         return int(ans)

#     def removeleadingzero(self, s: str) -> str:
#         iter = 0
#         for ch in s:
#             if(ch == 0):
#                 iter += 1
#             else:
#                 break
#         return s[iter:]

