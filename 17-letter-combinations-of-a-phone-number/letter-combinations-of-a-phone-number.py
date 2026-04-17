class Solution:
    keypad = {
        '2': "abc", '3': "def", '4': "ghi",
        '5': "jkl", '6': "mno", '7': "pqrs",
        '8': "tuv", '9': "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        ans = []

        def backtrack(index: int, path: str):
            if index == len(digits):
                ans.append(path)
                return

            current_digit = digits[index]

            for ch in self.keypad[current_digit]:
                backtrack(index + 1, path + ch)

        backtrack(0, "")
        return ans