#include <iostream>
#include <vector>
using namespace std;

// Linear Search Function
int linearSearch(const vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target)
            return i;
    }
    return -1;
}

// Binary Search Function (Iterative)
// NOTE: Array must be sorted
int binarySearch(const vector<int>& arr, int target) {
    int low = 0;
    int high = arr.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

int main() {
    vector<int> arr = {1, 3, 5, 7, 9, 11};
    int target = 7;

    cout << "Linear Search Result: "
         << linearSearch(arr, target) << endl;

    cout << "Binary Search Result: "
         << binarySearch(arr, target) << endl;

    return 0;
}
