class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix += chars[0]
            else:
                break
                
        return prefix

        # commonprefix = ""
        # smallestprefix = min(strs, key=len)
        # for i in smallestprefix:
        #     for str in strs:
        #         if i != str[len(commonprefix)]:
        #             return commonprefix
        #     commonprefix += i
        # return commonprefix
