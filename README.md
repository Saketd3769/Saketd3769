
## Tic Tac Toe GUI using Tkinter library from python

This is a human vs human version with many functionalities depictded in below video



https://user-images.githubusercontent.com/75195084/126108713-2357f33e-52a1-486d-9c21-2138934969b5.mov



## Tic Tac Toe using Minimax Algorithm
### What is Minimax 
Minimax is a artificial intelligence applied in two player games, such as tic-tac-toe, checkers, chess and go. This games are known as zero-sum games, because in a mathematical representation: one player wins (+1) and other player loses (-1) or both of anyone not to win (0).

### How does it work
The algorithm search, recursively, the best move that leads the Max player to win or not lose (draw). It consider the current state of the game and the available moves at that state, then for each valid move it plays (alternating min and max) until it finds a terminal state (win, draw or lose).    


**Lets understand MINIMAX Algorithm Thruogh a Picture**
![1_VG79nxl-mJQrsp6p3q79qA--1-](https://user-images.githubusercontent.com/75195084/126124064-d58dc932-8163-417d-b698-76b2b8d29597.png)   



## What is Alpha Beta Pruning
Alpha–beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. It stops evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined move.  

***First lets see if the optimisation was worth it or not***


https://user-images.githubusercontent.com/75195084/126134797-f6ace1e0-272f-44b8-a591-71df58e7f948.mp4



**Lets see how Alpha Beta Pruning reduces time complexity**
![tictactoe-alphabeta-e8cb918f](https://user-images.githubusercontent.com/75195084/126125853-4b0f1506-55a5-4b8c-9bf7-742f863af41d.png)

**More generalised Alpha Beta Pruning**  
<img width="488" alt="Screenshot 2021-07-19 at 1 52 01 PM" src="https://user-images.githubusercontent.com/75195084/126127424-5f7f8449-92dc-4c58-8252-95022a850c2b.png">


## Problems faced-
> 1. The code was very slow because the minimax algorithm while checking every possibility was using changing the Tkinter Button which is very slow. So i created a temporary array which decreased the time a lot.  
> 2. Just giving +10,-10 while evaluating the board was not enough. To make the Minimax Algorithm I subtracted depth from +10 and added depth to -10 such that the algorithm will chose that move which have lower depth always.  
> 3. Using a 2-D 3 * 3 array was a using more lines and travering in it was also not good. So I used a 1-D array of size 9 which shortened the code a lot.
  


