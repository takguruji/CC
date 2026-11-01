
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <chrono>
using namespace std;
using namespace chrono;

// Partition function
int partition(int arr[], int low, int high) {

    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {

        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[high]);

    return i + 1;
}

// Deterministic Quick Sort
void quickSort(int arr[], int low, int high) {

    if (low < high) {

        int p = partition(arr, low, high);

        quickSort(arr, low, p - 1);
        quickSort(arr, p + 1, high);
    }
}

// Randomized Quick Sort
void randomizedQuickSort(int arr[], int low, int high) {

    if (low < high) {

        // Select random pivot
        int randomIndex = low + rand() % (high - low + 1);

        swap(arr[randomIndex], arr[high]);

        int p = partition(arr, low, high);

        randomizedQuickSort(arr, low, p - 1);
        randomizedQuickSort(arr, p + 1, high);
    }
}

// Print array
void printArray(int arr[], int n) {

    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";

    cout << endl;
}

int main() {

    int n;

    cout << "Enter number of elements: ";
    cin >> n;

    int arr1[n], arr2[n];

    cout << "Enter array elements: ";

    for (int i = 0; i < n; i++) {
        cin >> arr1[i];
        arr2[i] = arr1[i];
    }

    srand(time(0));

    // Deterministic Quick Sort
    auto start = high_resolution_clock::now();

    quickSort(arr1, 0, n - 1);

    auto end = high_resolution_clock::now();

    cout << "\nDeterministic Quick Sort:\n";
    printArray(arr1, n);

    cout << "Time: "
         << duration_cast<microseconds>(end - start).count()
         << " microseconds\n";


    // Randomized Quick Sort
    start = high_resolution_clock::now();

    randomizedQuickSort(arr2, 0, n - 1);

    end = high_resolution_clock::now();

    cout << "\nRandomized Quick Sort:\n";
    printArray(arr2, n);

    cout << "Time: "
         << duration_cast<microseconds>(end - start).count()
         << " microseconds\n";

    return 0;
}
