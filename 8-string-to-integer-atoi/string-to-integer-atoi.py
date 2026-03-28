class Solution:
    def myAtoi(self, s: str) -> int:
        #eleminating leading whitespaces
        s = s.strip()
        if not s:
            return 0
        #doing negative check
        neg = 1
        if(s[0] in ['-', '+']):
            if(s[0] == "-"):
                neg *= (-1)
            s = s[1:]
        if not s:
            return 0
        #removed leading zeroes
        s = self.removeleadingzero(s)

        if not s:
            return 0
        #readinglines
        ans = ""
        for i in s:
            if(i.isdigit()):
                ans += i
            else:
                break
        if not ans:
            return 0

        #performing roundoffs
        if(int(ans) > 2147483647 and neg == -1):
            return -2147483648
        if(int(ans) > 2147483647):
            return 2147483647
        if(neg == -1):
            return int(ans)*(-1)
        return int(ans)

    def removeleadingzero(self, s: str) -> str:
        iter = 0
        for ch in s:
            if(ch == 0):
                iter += 1
            else:
                break
        return s[iter:]

