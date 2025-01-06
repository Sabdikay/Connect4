# Connect Four in Python

This repository contains **two versions** of a Connect Four game implemented in Python:

1. **Connect4 (Two Human Players)**  
2. **Connect4 (AI Player)** featuring a **minimax**-based computer opponent.

Both versions retain the core Connect Four mechanics but differ in how the second player’s moves are decided.

---

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
   - [Connect4 (Two Human Players)](#connect4-two-human-players)  
   - [Connect4 (AI Player)](#connect4-ai-player)  
3. [Gameplay Rules](#gameplay-rules)  
4. [How to Run](#how-to-run)  
5. [File Structure](#file-structure)
6. [Future Enhancements](#future-enhancements)


---

## Overview

Connect Four is a classic two-player game where you drop discs into one of the columns, attempting to line up **four of your discs** in a row before your opponent does. This repository offers:

- A **traditional 2-player** mode (Human vs. Human).  
- An **AI-enhanced** mode (Human vs. Computer) using **minimax** with alpha-beta pruning, leveraging the `random` and `math` libraries.  

---

## Features

### Connect4 (Two Human Players)

- **Board Generation**  
  Creates a 6×7 grid by default using `generateField()`. You can customize row and column sizes via parameters.

- **Turn-Based Input**  
  Players (Player 0 = `"R"`, Player 1 = `"Y"`) alternate columns to drop their discs.

- **Winning/Tie Checks**  
  After each move, checks if **4 in a row** is formed (horizontally, vertically, or diagonally). If the board fills up, the result is a **tie**.

- **Simple Board Drawing**  
  Displays columns separated by `" | "` with a dashed line after each row.

### Connect4 (AI Player)

- **AI Opponent**  
  In this version, Player 1 is replaced with an **AI** that uses a **minimax** algorithm for strategic column selection.

- **Scoring & Evaluation**  
  The AI’s decision-making:
  - Considers potential winning moves.
  - Evaluates board states based on the number of aligned discs and the center-column advantage.
  - Searches multiple moves ahead (controlled by a `depth` parameter).

- **Random Element**  
  Some fallback decisions may involve the `random` library to break ties among equally strong moves.

- **Still Allows Board Customization**  
  The same row and column parameters can be adjusted for custom board sizes.

---

## Gameplay Rules

1. **Objective**  
   Get four of your discs in a row before your opponent does. The row can be:
   - Horizontal
   - Vertical
   - Diagonal (descending or ascending)

2. **Turn Order**  
   - Player 0 goes first with discs labeled `"R"`.  
   - Player 1 uses discs labeled `"Y"`.  
   - In the AI version, Player 1 is controlled by the minimax algorithm.

3. **Placement Rules**  
   - Choose a column (1-based index).
   - The disc drops in the **lowest empty row** of that column.
   - If the column is full, you’ll be asked to choose another one.

4. **Ending Conditions**  
   - A player achieves **4 in a row** → that player wins immediately.
   - The grid is full with no winner → **tie**.

---

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Sabdikay/Connect4.git
   cd Connect4
   ```

2. **Run the Desired Version**:
   - **Two Human Players**:
     ```bash
     python Connect4.py
     ```
   - **AI Player**:
     ```bash
     python Connect4(AI player).py
     ```

3. **Play the Game**:
   - Input the column when prompted.
   - For the AI version, watch as the computer chooses an optimal (or near-optimal) move.

4. **Customize Board Dimensions** (Optional):
   - In either file, you can call `startGame(nrow, ncol)` with custom values:
     ```python
     startGame(8, 9)  # 8 rows, 9 columns
     ```

---

## File Structure

```
Connect4/
├── Connect4.py            # Two Human Players
├── Connect4(AI player).py # Computer Player using Minimax
├── README.md              # This README
```

- **`Connect4.py`**  
  Implements the standard 2-player logic.
  
- **`Connect4(AI player).py`**  
  Contains the AI logic using minimax with helper functions (`evaluateField`, `minimax`, etc.).

---

## Future Enhancements

- **More Sophisticated AI**: Add a deeper search or a weighting system for more advanced strategic play.  
- **GUI Version**: Integrate a library like Pygame or tkinter for a graphical interface.  
- **Logging & Statistics**: Track win rates, average game length, and other useful data.

---


**Enjoy your game of Connect Four, whether you challenge a friend or our AI opponent!**
