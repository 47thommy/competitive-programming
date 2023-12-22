class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        m, n = len(mat), len(mat[0])
        i = j = direction = False

        for _ in range(m * n):
            result.append(mat[i][j])

            if direction == False: 
                if j == n - 1:
                    direction = True 
                    i += 1
                elif i == 0:
                    direction = True
                    j += 1
                else:
                    i -= 1
                    j += 1
            else: 
                if i == m - 1:
                    direction = False
                    j += 1
                elif j == 0:
                    direction = False 
                    i += 1
                else:
                    i += 1
                    j -= 1

        
        return result