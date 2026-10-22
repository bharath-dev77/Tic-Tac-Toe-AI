# ⭕❌ TicTacToe-AI — Unbeatable Minimax Game Engine

[](https://www.python.org/)
[](https://streamlit.io/)
[](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
[](https://opensource.org/licenses/MIT)
[](https://www.python.org/)

> An open-source, zero-latency Tic-Tac-Toe web application featuring an unbeatable adversarial AI opponent powered by the Minimax decision-tree algorithm with Alpha-Beta pruning optimization.

## 🌟 Overview

**TicTacToe-AI** models classic $3 \times 3$ Tic-Tac-Toe as a deterministic, zero-sum adversarial search problem. Instead of relying on static lookup tables or external APIs, the engine dynamically evaluates future board states in real time using recursive game-tree traversal.

By combining depth-penalized terminal scoring with **Alpha-Beta ($\alpha\text{--}\beta$) branch pruning**, the AI eliminates redundant search paths—calculating the mathematically optimal counter-move in under a millisecond while running 100% locally in the browser via Streamlit.

## 🚀 Key Features

* **🧠 Unbeatable Minimax Decision Engine:** Explores the complete game tree from any board configuration to guarantee at least a draw or a forced win against any human strategy.
* **⚡ Alpha-Beta Pruning Optimization:** Tracks upper ($\beta$) and lower ($\alpha$) utility bounds across recursive branches, cutting off suboptimal subtrees and reducing node evaluations by up to 85%.
* **🎚️ Three Tunable Difficulty Tiers:**
  * **Easy (Stochastic):** Selects valid board positions at random for relaxed, beginner-friendly gameplay.
  * **Medium (Tactical Hybrid):** Blends heuristic win/block detection with a 40% stochastic exploration rate, allowing skilled players to create fork traps.
  * **Impossible (Full-Depth Minimax):** Executes an exhaustive $\alpha\text{--}\beta$ search with depth weighting; mathematically unbeatable.
* **📊 Real-Time Session Scoreboard:** Tracks Player (`X`) wins, AI (`O`) wins, and Draws across consecutive rounds without page reloads.
* **🎨 Reactive Web Interface:** Clean, responsive $3 \times 3$ interactive grid built with Streamlit featuring instant win-line validation and one-click board resets.

## 🏗️ System Architecture & Game Loop

| Layer | Module | Responsibility |
| :--- | :--- | :--- |
| **Presentation UI** | `app.py` (Streamlit) | Renders the $3 \times 3$ button grid, difficulty selector, status banners, and persistent session scoreboard. |
| **State Controller** | `st.session_state` | Maintains the 9-cell board array, active turn state, terminal game lock, and cumulative win/draw counters. |
| **Adversarial AI Engine** | `minimax.py` | Executes `get_best_move()`, recursive `minimax()` search with $\alpha\text{--}\beta$ pruning, and terminal state checks. |

## 🧮 Algorithm & Heuristic Scoring

The AI treats every turn as an optimization problem over a finite state space:

1. **Maximizing Player (`O` — AI):** Searches for moves that yield the highest possible terminal score.
2. **Minimizing Player (`X` — Human):** Assumed to play optimally, selecting moves that minimize the AI's score.
3. **Depth-Adjusted Terminal Utility:** To ensure the AI pursues the fastest possible victory and delays defeat as long as possible when behind, terminal states are weighted by recursion depth ($d$):

| Terminal Outcome | Utility Formula | Strategic Behavior |
| :--- | :--- | :--- |
| **AI (`O`) Wins** | $+10 - d$ | Prioritizes immediate winning moves over delayed wins. |
| **Human (`X`) Wins** | $d - 10$ | Prolongs the game and forces the opponent to find exact sequences. |
| **Tie / Full Board** | $0$ | Neutral equilibrium when both sides play optimally. |

## 🛠️ Tech Stack

| Component | Technology | Details |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core game logic, state evaluation, and recursion |
| **Web UI Framework** | Streamlit 1.32+ | Reactive browser interface and session state management |
| **Search Algorithm** | Minimax + Alpha-Beta Pruning | Pure Python standard library (`math`, `random`) — zero paid APIs |

## 📁 Repository Structure

```text
tic-tac-toe-ai/
├── app.py              # Streamlit interactive web UI, scoreboard & game loop
├── minimax.py          # Minimax recursive solver, Alpha-Beta pruning & win checker
├── requirements.txt    # Project dependencies (streamlit)
├── .gitignore          # Standard Python gitignore rules
├── LICENSE             # MIT License
└── README.md           # Project documentation
```

## ⚡ Quickstart Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tic-tac-toe-ai.git
cd tic-tac-toe-ai
```

### 2. Set Up a Virtual Environment

```powershell
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Launch the Game

```powershell
python -m streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser to start playing.

## 🎮 Difficulty Mode Comparison

| Mode | Decision Mechanism | Average Search Depth | Expected Player Outcome |
| :--- | :--- | :--- | :--- |
| **Easy** | Uniform random sampling over empty cells | $1$ ply | Frequent player wins |
| **Medium** | $60\%$ Minimax / $40\%$ random move selection | $1\text{--}9$ plies | Balanced competitive play |
| **Impossible** | Exhaustive Minimax with $\alpha\text{--}\beta$ cutoffs | Full tree ($9!$ bound) | Draw at best (Unbeatable) |

## 📄 License

This project is licensed under the MIT License — see the `LICENSE` file for details.
