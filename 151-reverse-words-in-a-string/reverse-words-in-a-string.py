class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split()
        words_list.reverse()
        single_string = " ".join(words_list)
        return single_string