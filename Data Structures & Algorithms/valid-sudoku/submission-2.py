class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxMap = defaultdict(set) 
        colMap = defaultdict(set) 
        rowMap = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue

                if board[r][c] in boxMap[(r//3,c//3)] or board[r][c] in rowMap[r] or board[r][c] in colMap[c]:
                    return False
                else:
                    rowMap[r].add(board[r][c])
                    colMap[c].add(board[r][c])
                    boxMap[(r//3,c//3)].add(board[r][c])
        return True

                 
