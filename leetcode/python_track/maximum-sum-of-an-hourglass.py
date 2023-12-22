class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                temp = 0
                for k in range(3):
                    for t in range(3):    
                        if k==0 or k==2 or (k==1 and t==1):
                            temp = temp + grid[i+k][j+t]      
                ans = max(ans, temp)
        return ans