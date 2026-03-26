class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonprefix = ""
        smallestprefix = min(strs, key=len)
        for i in smallestprefix:
            for str in strs:
                if i not in str[len(commonprefix)]:
                    return commonprefix
            commonprefix += i
        return commonprefix
