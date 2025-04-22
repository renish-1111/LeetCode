class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        res = [[1],[1,1]]

        for i in range(2,numRows):
            row = [1]
            for j in range(1,i):
                row.append(res[i-1][j] + res[i-1][j-1])
            row.append(1)
            res.append(row)
        
        return res