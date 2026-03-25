class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [0, 0]
        row = len(mat)

        for i in range(row):
            count = sum(mat[i])
            if count > res[1]:
                res[0] = i
                res[1] = count
        return res 