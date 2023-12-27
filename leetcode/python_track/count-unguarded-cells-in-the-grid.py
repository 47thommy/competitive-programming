class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        unseen = [[1]*n for _ in range(m)]
        result = m*n

        for r, c in walls + guards:
            unseen[r][c] = 0
            result -= 1
        
        for gr, gc in guards:
            for bc in range(gc-1, -1, -1):
                if unseen[gr][bc] == 1:
                    unseen[gr][bc] = -1
                    result -= 1
                elif unseen[gr][bc] == 0:
                    break

            for bc in range(gc+1, n):
                if unseen[gr][bc] == 1:
                    unseen[gr][bc] = -1
                    result -= 1
                elif unseen[gr][bc] == 0:
                    break

            for br in range(gr-1, -1, -1):
                if unseen[br][gc] == 1:
                    unseen[br][gc] = -1
                    result -= 1
                elif unseen[br][gc] == 0:
                    break

            for br in range(gr+1, m):
                if unseen[br][gc] == 1:
                    unseen[br][gc] = -1
                    result -= 1
                elif unseen[br][gc] == 0:
                    break

        return result
