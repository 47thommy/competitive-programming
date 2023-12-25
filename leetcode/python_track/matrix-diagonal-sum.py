class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        lr=0
        rl=0
        i,j=0,0
        while i<len(mat) and j<len(mat):
            lr+=mat[i][j]
            i+=1
            j+=1
        k,l=0,len(mat)-1
        while k<len(mat) and l>=0:
            rl+=mat[k][l]
            k+=1
            l-=1
        if len(mat)%2!=0:
            return rl+lr-mat[len(mat)//2][len(mat)//2]
        else:
            return rl+lr
                           
                           