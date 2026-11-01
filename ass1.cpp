#include <iostream>
using namespace std;

int fibonacci(int n) {
    if ( n == 0) return 0;
    if ( n == 1) return 1 ;
    if ( n > 1 ) return fibonacci(n-1) + fibonacci(n-2);
}

int main() {
    cout<<" enter a number"<<endl;
    int n;
    cin>> n;

    cout<< "fibonacci series"<<endl;
    for( int i = 0 ; i < n;i++){
        cout<< fibonacci(i) << " ";
    }

}



#include <iostream>
using namespace std;

int main() {
    int n;

    cout << "Enter number of terms: ";
    cin >> n;

    int a = 0, b = 1, c;

    cout << "Fibonacci Series: ";

    for (int i = 0; i < n; i++) {
        cout << a << " ";

        c = a + b;
        a = b;
        b = c;
    }

    return 0;
}
