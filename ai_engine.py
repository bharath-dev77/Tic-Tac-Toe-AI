"""
ai_engine.py — Rule-Based Decision Engine

The core AI component. Given a Board and the two marks in play,
it returns a single cell index to play — chosen by walking a
fixed priority ladder, top to bottom, and stopping at the first
rule that applies:

    1. Win     — play a move that completes three in a row
    2. Block   — stop the opponent from winning next turn
    3. Center  — take the middle cell if it's free
    4. Corner  — prefer a corner over an edge
    5. Random  — otherwise, take any free cell

No search, no training, no memory of past games — every decision
is derived fresh from the current board state.
"""

import random

CENTER = 4
CORNERS = (0, 2, 6, 8)


class RuleBasedAI:
    def __init__(self, ai_mark="O", player_mark="X"):
        self.ai_mark = ai_mark
        self.player_mark = player_mark

    def choose_move(self, board):
        return (
            self._find_winning_move(board, self.ai_mark)      # Rule 1: Win
            or self._find_winning_move(board, self.player_mark)  # Rule 2: Block
            or self._take_center(board)                       # Rule 3: Center
            or self._take_corner(board)                       # Rule 4: Corner
            or self._take_random(board)                       # Rule 5: Random
        )

    def _find_winning_move(self, board, mark):
        """Returns a cell that would give `mark` three in a row, if one exists."""
        for cell in board.get_empty_cells():
            trial = board.copy_cells()
            trial[cell] = mark
            if self._has_won(trial, mark):
                return cell
        return None

    def _take_center(self, board):
        return CENTER if board.is_empty(CENTER) else None

    def _take_corner(self, board):
        free_corners = [c for c in CORNERS if board.is_empty(c)]
        return random.choice(free_corners) if free_corners else None

    def _take_random(self, board):
        empty = board.get_empty_cells()
        return random.choice(empty) if empty else None

    @staticmethod
    def _has_won(cells, mark):
        from board import WIN_LINES
        return any(cells[a] == cells[b] == cells[c] == mark for a, b, c in WIN_LINES)
