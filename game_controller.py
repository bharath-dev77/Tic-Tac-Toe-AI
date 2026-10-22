"""
game_controller.py — Game Controller

Coordinates the pieces: it holds the Board State Manager and the
Rule-Based Decision Engine, enforces turn order, validates moves,
and acts as the Move Executor — writing the chosen cell to the
board and reporting the result back to the User Interface.
"""

from board import Board
from ai_engine import RuleBasedAI

PLAYER_MARK = "X"
AI_MARK = "O"


class GameController:
    def __init__(self):
        self.board = Board()
        self.ai = RuleBasedAI(ai_mark=AI_MARK, player_mark=PLAYER_MARK)
        self.game_over = False

    def new_game(self):
        self.board.reset()
        self.game_over = False

    def player_move(self, index):
        """
        Attempts to place the player's mark at `index`.
        Returns a status dict the UI can render directly.
        """
        if self.game_over or not self.board.is_empty(index):
            return self._status(moved=False)

        self.board.place(index, PLAYER_MARK)

        if self.board.is_game_over():
            self.game_over = True
            return self._status(moved=True)

        # AI takes its turn immediately after a valid player move
        ai_index = self.ai.choose_move(self.board)
        self.board.place(ai_index, AI_MARK)

        if self.board.is_game_over():
            self.game_over = True

        return self._status(moved=True, ai_index=ai_index)

    def _status(self, moved, ai_index=None):
        return {
            "moved": moved,
            "ai_index": ai_index,
            "cells": self.board.copy_cells(),
            "winner": self.board.winner(),
            "winning_line": self.board.winning_line(),
            "is_draw": self.board.is_draw(),
            "game_over": self.game_over,
        }
