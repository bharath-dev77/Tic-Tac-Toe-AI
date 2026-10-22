"""
ui.py — User Interface (Tkinter)

Purely presentational: draws the 3x3 grid of buttons and a status
label, forwards clicks to the Game Controller, and re-renders
whatever status dict comes back. No game rules live here.
"""

import tkinter as tk
from tkinter import font as tkfont

from game_controller import GameController

MARK_COLORS = {"X": "#FF6B35", "O": "#415A77"}
WIN_HIGHLIGHT = "#E8EAED"


class TicTacToeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI — Rule-Based Opponent")
        self.root.configure(bg="#1B263B")

        self.controller = GameController()
        self.buttons = []

        self.cell_font = tkfont.Font(family="Calibri", size=28, weight="bold")
        self.status_font = tkfont.Font(family="Calibri", size=13)

        self._build_widgets()
        self._render(self.controller.board.copy_cells())

    def _build_widgets(self):
        self.status_label = tk.Label(
            self.root, text="Your turn — you are X",
            font=self.status_font, bg="#1B263B", fg="white", pady=10,
        )
        self.status_label.grid(row=0, column=0, columnspan=3)

        grid_frame = tk.Frame(self.root, bg="#1B263B")
        grid_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

        for i in range(9):
            btn = tk.Button(
                grid_frame, text="", font=self.cell_font, width=4, height=2,
                bg="white", activebackground="#F8F9FA", relief="flat",
                command=lambda i=i: self._on_cell_click(i),
            )
            btn.grid(row=i // 3, column=i % 3, padx=3, pady=3)
            self.buttons.append(btn)

        restart_btn = tk.Button(
            self.root, text="New Game", font=self.status_font,
            bg="#FF6B35", fg="white", relief="flat", command=self._on_restart,
        )
        restart_btn.grid(row=2, column=0, columnspan=3, pady=15)

    def _on_cell_click(self, index):
        result = self.controller.player_move(index)
        if not result["moved"]:
            return
        self._render(result["cells"], result["winning_line"])
        self._update_status(result)

    def _on_restart(self):
        self.controller.new_game()
        self._render(self.controller.board.copy_cells())
        self.status_label.config(text="Your turn — you are X")

    def _render(self, cells, winning_line=None):
        for i, btn in enumerate(cells):
            mark = cells[i]
            self.buttons[i].config(
                text=mark, fg=MARK_COLORS.get(mark, "black"),
                state="disabled" if mark else "normal",
                bg=WIN_HIGHLIGHT if winning_line and i in winning_line else "white",
            )

    def _update_status(self, result):
        if result["winner"] == "X":
            self.status_label.config(text="You win! 🎉")
        elif result["winner"] == "O":
            self.status_label.config(text="AI wins — try again!")
        elif result["is_draw"]:
            self.status_label.config(text="It's a draw!")
        else:
            self.status_label.config(text="Your turn — you are X")


def launch():
    root = tk.Tk()
    TicTacToeUI(root)
    root.mainloop()
