  1. Minimax Algorithm (Most Common):
The Minimax algorithm is a decision-making algorithm, perfect for two-player games like Tic-Tac-Toe. It aims to minimize the possible loss in a worst-case scenario, hence the name "minimax."

How it works:
The AI recursively simulates all possible moves and their outcomes.
It assumes the opponent is also playing optimally.
For every possible move, the AI calculates a score that reflects the potential result (win, lose, or draw).
It chooses the move that maximizes its own score while minimizing the opponent’s score.
Steps in the Minimax Algorithm:

Maximizer's move (AI’s turn): AI tries to maximize the score.
Minimizer's move (human’s turn): AI assumes the human will minimize the AI's score.
The algorithm explores all the game states and picks the best move for the AI.
Advantages:

It ensures the AI never loses.
It explores all possible outcomes to guarantee the best move.
Disadvantages:

For larger games, Minimax can be slow since it checks all possibilities (but Tic-Tac-Toe is small enough for it to be efficient).
2. Alpha-Beta Pruning (Improvement on Minimax):
Alpha-Beta Pruning is an optimization technique for Minimax, where branches of the game tree that don't need exploration (because they won’t affect the outcome) are cut off. This reduces computation time while maintaining the same result.

3. Rule-Based AI:
A simpler approach might involve hardcoded strategies:

First move: If the center square is free, take it.
Win or Block: If the AI or human has two in a row, place the third to win or block.
Forking: Create opportunities where the AI can win in multiple ways
