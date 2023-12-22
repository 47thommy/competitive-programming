from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        sub_boards = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element == ".":
                    continue
 
                if (element in rows[r] or 
                    element in columns[c] or 
                    element in sub_boards[(r // 3, c // 3)]):
                        return False

                rows[r].add(element)
                columns[c].add(element)
                sub_boards[(r // 3, c // 3)].add(element)

        return True
