"""
board.py — Board State Manager

Owns the 3x3 grid and all state queries: empty cells, win checks,
draw checks. Knows nothing about players, turns, or the AI —
it only reports what the board currently looks like.
"""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]

EMPTY = ""


class Board:
    def __init__(self):
        self.cells = [EMPTY] * 9

    def reset(self):
        self.cells = [EMPTY] * 9

    def get_empty_cells(self):
        return [i for i, v in enumerate(self.cells) if v == EMPTY]

    def is_empty(self, index):
        return self.cells[index] == EMPTY

    def place(self, index, mark):
        """Move Executor calls this to write a mark to the board."""
        if not self.is_empty(index):
            raise ValueError(f"Cell {index} is already occupied")
        self.cells[index] = mark

    def is_full(self):
        return EMPTY not in self.cells

    def winner(self):
        """Returns 'X', 'O', or None."""
        for a, b, c in WIN_LINES:
            if self.cells[a] != EMPTY and self.cells[a] == self.cells[b] == self.cells[c]:
                return self.cells[a]
        return None

    def winning_line(self):
        """Returns the winning triple of indices, or None (used to highlight the UI)."""
        for a, b, c in WIN_LINES:
            if self.cells[a] != EMPTY and self.cells[a] == self.cells[b] == self.cells[c]:
                return (a, b, c)
        return None

    def is_draw(self):
        return self.winner() is None and self.is_full()

    def is_game_over(self):
        return self.winner() is not None or self.is_full()

    def copy_cells(self):
        return list(self.cells)
