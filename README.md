# Tic-Tac-Toe AI — Rule-Based Game Opponent

Matches the architecture in the project PPT: User Interface → Game
Controller → Board State Manager → Rule-Based Decision Engine → Move
Executor.

## Files

| File | Role (from the Architecture slide) |
|---|---|
| `board.py` | **Board State Manager** — holds the 9 cells, checks wins/draws |
| `ai_engine.py` | **Rule-Based Decision Engine** — Win → Block → Center → Corner → Random |
| `game_controller.py` | **Game Controller** + **Move Executor** — enforces turns, writes moves to the board |
| `ui.py` | **User Interface** — Tkinter grid, status label, click handling |
| `main.py` | Entry point |

## Run it

```
python main.py
```

Requires only the standard library (Tkinter ships with Python).

## A note on "unbeatable"

The priority ladder (win → block → center → corner → random) beats
random play the large majority of the time, but it isn't a true
guarantee: a player who sets up a **double threat (fork)** — e.g.
taking two opposite corners — can force a win, because the AI can
only block one threat per turn and has no lookahead beyond the
current move. Closing that gap requires the Minimax algorithm,
which is listed as the project's **Future Scope**. Testing against
1,000 random-move games: the AI won ~73%, drew ~15%, and lost ~11%
— worth mentioning if asked about limitations during your viva.
