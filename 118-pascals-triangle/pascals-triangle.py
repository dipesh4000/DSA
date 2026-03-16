
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        count = 0
        
        while count < numRows:
            row = []
            
            for i in range(count + 1):
                if i == 0 or i == count:
                    row.append(1)
                else:
                    row.append(result[count-1][i] + result[count-1][i-1])
            
            result.append(row)
            count += 1
        
        return result