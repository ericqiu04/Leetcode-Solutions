import collections
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        boxes = collections.defaultdict(set)
        column = collections.defaultdict(set)
        rows = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if (board[row][col] == "."):
                    continue
                if (board[row][col] in column[col] or board[row][col] in rows[row] or board[row][col] in boxes[
                    (row // 3), (col // 3)]):
                    return False

                rows[row].add(board[row][col])
                column[col].add(board[row][col])
                boxes[(row // 3, (col // 3))].add(board[row][col])

        return True