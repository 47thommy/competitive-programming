class Solution:
    def totalNQueens(self, n: int) -> int:
        row=set()
        col=set()
        mainD=set()
        antiD=set()
        res=set()
        board=[["."] * n for i in range(n)]
        print(board)
        def backtrack(r):
            if r == n:
                ans= ["".join(row) for row in board]
                res.add(tuple(ans))
                return
            for c in range(n):
                if c in col or r+c in mainD or r-c in antiD:
                    continue
                col.add(c)
                mainD.add(r+c)
                antiD.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1)
                col.remove(c)
                mainD.remove(r+c)
                antiD.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return len(res)