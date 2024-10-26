class SudokuSolver:
    def __init__(self, board: list[list[int]]):
        self.board = board

    def __repr__(self):
        return f'SudokuSolver(board={self.board})'

    def __solve(self):
        if not (empty_pos := self.__find_empty()):
            return True
        row, col = empty_pos
        for i in range(1, 10):
            if self.__is_valid(number=i, row=row, col=col):
                self.board[row][col] = i
                if self.__solve():
                    return True
                self.board[row][col] = 0
        return False

    def __find_empty(self) -> tuple[int, int] | None:
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def __is_valid(self, row: int, col: int, number: int) -> bool:
        for i in range(9):
            if self.board[row][i] == number:
                return False
            elif self.board[i][col] == number:
                return False

        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == number:
                    return False

        return True

    def solve(self) -> list[list[int]]:
        self.__solve()
        return self.board

    def __call__(self) -> list[list[int]] | None:
        return self.solve()
