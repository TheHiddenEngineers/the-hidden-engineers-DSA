#include <bits/stdc++.h>
using namespace std;

// FIXED SLIDING WINDOW
// Maximum sum of subarray of size k
int maxSumSubarray(vector<int>& arr, int k) {
    int n = arr.size();
    if (n < k) return -1;

    int windowSum = 0;
    for (int i = 0; i < k; i++)
        windowSum += arr[i];

    int maxSum = windowSum;

    for (int i = k; i < n; i++) {
        windowSum += arr[i];       // add right element
        windowSum -= arr[i - k];   // remove left element
        maxSum = max(maxSum, windowSum);
    }

    return maxSum;
}

int main() {
    vector<int> arr = {2, 1, 5, 1, 3, 2};
    int k = 3;

    cout << "Max Sum of Subarray of size k: "
         << maxSumSubarray(arr, k) << endl;

    return 0;
}
