// Day 5 - Kadane's Algorithm
// Topic: Maximum Subarray Sum
// Covers:
// 1. Brute Force intuition
// 2. Why negative reset matters
// 3. Kadane's Algorithm
// 4. Edge cases

#include <bits/stdc++.h>
using namespace std;

int maxSubarraySum(vector<int>& arr) {
    int currentSum = 0;
    int maxSum = arr[0];  // important for all-negative case

    for (int i = 0; i < arr.size(); i++) {
        currentSum += arr[i];
        maxSum = max(maxSum, currentSum);

        // reset if sum becomes negative
        if (currentSum < 0)
            currentSum = 0;
    }

    return maxSum;
}

int main() {

    vector<int> arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};

    cout << "Maximum Subarray Sum: "
         << maxSubarraySum(arr) << endl;

    return 0;
}
