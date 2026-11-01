
#include <iostream>
using namespace std;

int n = 4;
int board[10][10] = {0};

// Check whether queen can be placed
bool isSafe(int row, int col) {

    // Check same column
    for (int i = 0; i < row; i++) {
        if (board[i][col] == 1)
            return false;
    }

    // Check left diagonal
    for (int i = row-1, j = col-1; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 1)
            return false;
    }

    // Check right diagonal
    for (int i = row-1, j = col+1; i >= 0 && j < n; i--, j++) {
        if (board[i][j] == 1)
            return false;
    }

    return true;
}

// Solve using Backtracking
bool solve(int row) {

    if (row == n)
        return true;

    for (int col = 0; col < n; col++) {

        if (isSafe(row, col)) {

            board[row][col] = 1;

            if (solve(row + 1))
                return true;

            board[row][col] = 0; // Backtrack
        }
    }

    return false;
}

int main() {

    // Place first queen
    board[0][1] = 1;

    if (solve(1)) {

        cout << "Solution:\n";

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }

    } else {
        cout << "No solution exists";
    }

    return 0;
}
