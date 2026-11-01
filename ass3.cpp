
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n = 4;
    int capacity = 8;

    int weight[] = {1, 3, 4, 5};
    int profit[] = {10, 40, 50, 70};

    int dp[5][9] = {0};

    // Dynamic Programming
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {

            if (weight[i-1] <= w) {
                dp[i][w] = max(
                    profit[i-1] + dp[i-1][w-weight[i-1]],
                    dp[i-1][w]
                );
            }
            else {
                dp[i][w] = dp[i-1][w];
            }
        }
    }

    cout << "Maximum Profit: "
         << dp[n][capacity] << endl;

}
