
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n , capacity;
    cout << "Enter number of items: ";
    cin >> n;


    int weight[n], profit[n];

    cout << "Enter weights:\n";
    for (int i = 0; i < n; i++)
        cin >> weight[i];

    cout << "Enter profits:\n";
    for (int i = 0; i < n; i++)
        cin >> profit[i];

    cout << "Enter knapsack capacity: ";
    cin >> capacity;


    vector<vector<int>> dp(n+1, vector<int>(capacity+1, 0));

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
