#include <stdio.h>
char shape(int i) 
{
    switch(i) 
    {
        case -1:
            return 'X';
        case 0:
            return ' ';
        case 1:
            return 'O';
    }
}
void draw(int b[9]) 
{
    printf(" %c | %c | %c\n",shape(b[0]),shape(b[1]),shape(b[2]));
    printf("---+---+---\n");
    printf(" %c | %c | %c\n",shape(b[3]),shape(b[4]),shape(b[5]));
    printf("---+---+---\n");
    printf(" %c | %c | %c\n",shape(b[6]),shape(b[7]),shape(b[8]));
}
int win_loss(const int board[9]) 
{
    unsigned wins[8][3] = {{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}};
    int i;
    for(i = 0; i < 8; ++i) 
    {
        if(board[wins[i][0]] != 0 && board[wins[i][0]] == board[wins[i][1]] && board[wins[i][0]] == board[wins[i][2]]) 
	    return board[wins[i][2]];
    }
    return 0;
}
int minimax(int board[9], int player) 
{
    int winner = win_loss(board);
    if(winner != 0) 
	return winner*player;
    int move = -1;
    int score = -2;
    int i;
    for(i = 0; i < 9; ++i) 
    {
        if(board[i] == 0) 
	{
            board[i] = player;
            int thisScore = -minimax(board, player*-1);
            if(thisScore > score) 
	    {
                score = thisScore;
                move = i;
            }
            board[i] = 0;
        }
    }
    if(move == -1) return 0;
    return score;
}
void comp_move(int board[9]) 
{
    int move = -1;
    int score = -2;
    int i;
    for(i = 0; i < 9; ++i) {
        if(board[i] == 0) {
            board[i] = 1;
            int tempScore = -minimax(board, -1);
            board[i] = 0;
            if(tempScore > score) {
                score = tempScore;
                move = i;
            }
        }
    }
    board[move] = 1;
}
void player_move(int board[9]) 
{
    int move = 0;
    do {
        printf("\nInput move ([0..8]): ");
        scanf("%d", &move);
        printf("\n");
    } while (move >= 9 || move < 0 && board[move] == 0);
    board[move] = -1;
}
int main() 
{
    int board[9] = {0,0,0,0,0,0,0,0,0};
    printf("Do you want to play first(1) or second(2)?:");
    int player=0;
    scanf("%d",&player);
    printf("\n");
    int turn;
    for(turn = 0; turn < 9 && win_loss(board) == 0; ++turn) 
    {
        if((turn+player) % 2 == 0)
            comp_move(board);
        else 
	{
            draw(board);
            player_move(board);
        }
    }
    switch(win_loss(board))
    {
        case 0:
            printf("Tie!\n");
        break;
        case 1:
            draw(board);
            printf("You lose!\n");
        break;
        case -1:
            printf("You win!\n");
        break;
    }
}
