# ai-system-ExWhyZedd

A Game
Playing Agent for
ExWhyZedd
Artificial Intelligence
November 23rd, 2018
TEAM MEMBERS
Kaushik Ravi - 01FB16ECS160
Keertan Krishnan - 01FB16ECS163
Kevin Paul - 01FB16ECS166
2
Table Of Contents
Introduction 3
Overview 3
Game Description 3
Goals 4
Solver Techniques - Overview 5
Solver Techniques - Implementation 6
Results 7
Conclusion 8
3
Introduction
This project was done by B.Tech students of PES University, Bangalore, India
as part of Artificial Intelligence (UE16CS) course during the August -
December(Fall) semester of 2018, under the guidance of Dr. Ramesh Bhat,
faculty, PES University CSE department.
Overview
Artificial intelligence is a science and technology based on disciplines such
as Computer Science, Biology, Psychology, Linguistics, Mathematics, and
Engineering. A major thrust of AI is in the development of computer
functions associated with human intelligence, such as reasoning, learning,
and problem solving. In the field of Computer Science, Artificial Intelligence
involves the study of intelligent agents, a device that perceives its
environment and takes actions that maximize it’s chance of successfully
achieve its goals. The aim of this course is to familiarize students with the
concepts of artificial intelligence.
4
Game Description
ExWhyZedd is a paper-and-pencil game for three players, each of whom play
one move in succession, with the symbols X, Y and Z respectively, and take
turns marking the spaces in a 5×5 grid. The player who succeeds in placing
four of their marks in a horizontal, vertical, or diagonal row wins the game.
This is a game similar in play sequence to Tic-Tac-Toe, with a crucial
difference. The board is represented in 2 dimensions, however, the board is
in reality spherical in shape, with the edges and corners wrapping around to
meet one another.
Goals
● To understand the fundamental workings of the underlying logic of the
game ExWhyZedd, in the process developing an intuitional algorithm
for optimal gameplay
● To express this algorithm for gameplay in the form of a game tree, and
an evaluation function, which can then be solved
● To develop an intelligent agent capable of playing the game
ExWhyZedd in an optimal manner
5
Solver Techniques - Overview
● Minimax Algorithm
Minimax is a kind of backtracking algorithm that is used in decision
making and game theory to find the optimal move for a player,
assuming that your opponent also plays optimally. It is widely used in
two player turn-based games such as Tic-Tac-Toe, Backgammon,
Mancala, Chess, etc.
In Minimax the two players are called maximizer and minimizer. The
maximizer tries to get the highest score possible while the minimizer
tries to do the opposite and get the lowest score possible.
Every board state has a value associated with it. In a given state if the
maximizer has upper hand then, the score of the board will tend to be
some positive value. If the minimizer has the upper hand in that board
state then it will tend to be some negative value. The values of the
board are calculated by some heuristics which are unique for every
type of game.
6
● Alpha - Beta pruning
Alpha-Beta pruning is not actually a new algorithm, rather an
optimization technique for minimax algorithm. It reduces the
computation time by a huge factor. This allows us to search much
faster and even go into deeper levels in the game tree. It cuts off
branches in the game tree which need not be searched because there
already exists a better move available. It is called Alpha-Beta pruning
because it passes 2 extra parameters in the minimax function, namely
alpha and beta.
● Evaluation Function
An evaluation function, also known as a heuristic evaluation function
or static evaluation function, is a function used by game-playing
programs to estimate the value or goodness of a position in the
minimax and related algorithms. The evaluation function is typically
designed to prioritize speed over accuracy; the function looks only at
the current position and does not explore possible moves, and is
therefore static.
7
Observations and Results
● The minimax algorithm alone was not able to play the game in the
most optimal manner.
● The evaluation function used was too primitive to play the game
optimally.
● As a case study, we used a similar minimax function to play the game
‘Tic Tac Toe’, which played the game in the most optimal manner.
● We concluded that the number of states in the game ExWhyZed was
simply too high to rely on a mathematically derived evaluation
function.
● As an improvement, we could build a Neural Network trained with
Game States, that would perform much better as an evaluation
function.

Execution instructions
Compile and run ttt.c in order to simulate an agent to play againt human. 
