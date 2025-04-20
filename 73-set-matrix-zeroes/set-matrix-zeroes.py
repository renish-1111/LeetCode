class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = []
        for i,row in enumerate(matrix):
            for j,val in enumerate(row):
                if val == 0:
                    res.append([i,j])
        
        for ind in res:
            self.up(matrix,ind[0],ind[1])
            self.down(matrix,ind[0],ind[1])
            self.left(matrix,ind[0],ind[1])
            self.right(matrix,ind[0],ind[1])


    def up(self,m,i,j):
        for k in range(i-1,-1,-1):
            m[k][j] = 0
    def down(self,m,i,j): 
        for k in range(i+1,len(m)):
            m[k][j] = 0   
    def left(self,m,i,j):  
        for k in range(j-1,-1,-1):
            m[i][k] = 0 
    def right(self,m,i,j):    
        for k in range(j+1,len(m[0])):
            m[i][k] = 0 
