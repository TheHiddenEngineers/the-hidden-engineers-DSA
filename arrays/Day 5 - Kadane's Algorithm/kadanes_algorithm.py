# Day 5 - Kadane's Algorithm
# Topic: Maximum Subarray Sum
# Covers:
# 1. Brute Force intuition
# 2. Why negative reset matters
# 3. Kadane's Algorithm
# 4. Edge cases

def max_subarray_sum(arr):
    current_sum = 0
    max_sum = arr[0]  # important for all-negative case

    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)

        # reset if sum becomes negative
        if current_sum < 0:
            current_sum = 0

    return max_sum


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum Subarray Sum:", max_subarray_sum(arr))
