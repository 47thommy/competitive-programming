class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        def transpose(matrix):
            ans=[]
            hashmap=defaultdict(list)

            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    hashmap[j].append(matrix[i][j])
            for value in hashmap.values():
                ans.append(value)
            return ans
        before=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                before+=grid[i][j]
        t=transpose(grid)
        for i in range(len(grid)):
            rowMax=max(grid[i])
            for j in range(len(grid[0])):
                grid[i][j]=rowMax
        for i in range(len(t)):
            for j in range(len(t[0])):
                rowMax=max(t[j])
                grid[i][j]=min(grid[i][j],rowMax)
        after=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                after+=grid[i][j]
        return after-before