class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows == n:
            return s

        arrString = [""] * numRows
        i = 0
        interval = 0

        while i < n:   
            arrString[interval] += s[i]
            if interval == 0:
                forward = True
            elif interval == numRows-1:
                forward = False
        
            if forward:
                interval += 1
            else:
                interval -= 1
            
            i+=1
        
        return "".join(arrString)