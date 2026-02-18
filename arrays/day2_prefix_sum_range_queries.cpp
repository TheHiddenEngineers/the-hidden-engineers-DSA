/*
    Day 2 – Prefix Sum + Range Queries
    -----------------------------------
    Concepts Covered:
    1. Brute Force vs Prefix Sum
    2. Preprocessing
    3. Range Sum Queries
    4. 2D Prefix Sum (Intro)
    5. Space-Time Tradeoff

    Author: Your Name
*/

#include <bits/stdc++.h>
using namespace std;

/* ================================
        1D PREFIX SUM
================================ */

// Builds prefix sum array
vector<long long> buildPrefix(const vector<int>& arr) {
    int n = arr.size();
    vector<long long> prefix(n);

    prefix[0] = arr[0];
    for (int i = 1; i < n; i++) {
        prefix[i] = prefix[i - 1] + arr[i];
    }

    return prefix;
}

// Returns sum in range [L, R]
long long rangeSum(const vector<long long>& prefix, int L, int R) {
    if (L == 0) return prefix[R];
    return prefix[R] - prefix[L - 1];
}


/* ================================
        2D PREFIX SUM
================================ */

// Builds 2D prefix sum matrix
vector<vector<long long>> build2DPrefix(const vector<vector<int>>& matrix) {
    int n = matrix.size();
    int m = matrix[0].size();

    vector<vector<long long>> prefix(n, vector<long long>(m, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {

            prefix[i][j] = matrix[i][j];

            if (i > 0)
                prefix[i][j] += prefix[i - 1][j];

            if (j > 0)
                prefix[i][j] += prefix[i][j - 1];

            if (i > 0 && j > 0)
                prefix[i][j] -= prefix[i - 1][j - 1];
        }
    }

    return prefix;
}

// Returns sum of submatrix from (r1, c1) to (r2, c2)
long long rangeSum2D(const vector<vector<long long>>& prefix,
                     int r1, int c1, int r2, int c2) {

    long long result = prefix[r2][c2];

    if (r1 > 0)
        result -= prefix[r1 - 1][c2];

    if (c1 > 0)
        result -= prefix[r2][c1 - 1];

    if (r1 > 0 && c1 > 0)
        result += prefix[r1 - 1][c1 - 1];

    return result;
}


/* ================================
              MAIN
================================ */

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // -------- 1D Example --------
    int n;
    cout << "Enter size of array: ";
    cin >> n;

    vector<int> arr(n);
    cout << "Enter elements:\n";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    vector<long long> prefix = buildPrefix(arr);

    int q;
    cout << "Enter number of range queries: ";
    cin >> q;

    while (q--) {
        int L, R;
        cout << "Enter L and R (0-indexed): ";
        cin >> L >> R;

        cout << "Range Sum = " << rangeSum(prefix, L, R) << "\n";
    }


    // -------- 2D Example --------
    int rows, cols;
    cout << "\nEnter rows and columns of matrix: ";
    cin >> rows >> cols;

    vector<vector<int>> matrix(rows, vector<int>(cols));
    cout << "Enter matrix elements:\n";

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> matrix[i][j];

    vector<vector<long long>> prefix2D = build2DPrefix(matrix);

    int r1, c1, r2, c2;
    cout << "Enter submatrix (r1 c1 r2 c2): ";
    cin >> r1 >> c1 >> r2 >> c2;

    cout << "Submatrix Sum = "
         << rangeSum2D(prefix2D, r1, c1, r2, c2) << "\n";

    return 0;
}
