class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowHash= defaultdict(set)
        columnHash= defaultdict(set)
        boxHash= defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] not in rowHash[r]:
                    rowHash[r].add(board[r][c] )
                else:
                    return False
                if board[r][c] not in columnHash[c]:
                    columnHash[c].add(board[r][c])
                else:
                    return False
                
                if board[r][c] not in boxHash[(r//3,c//3)]:
                    boxHash[(r//3,c//3)].add(board[r][c])
                else:
                    return False
        
        return True
