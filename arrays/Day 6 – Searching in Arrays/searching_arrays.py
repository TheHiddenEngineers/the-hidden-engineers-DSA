# Linear Search Function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Binary Search Function (Iterative)
# NOTE: Array must be sorted
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Driver Code
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    target = 7

    print("Linear Search Result:", linear_search(arr, target))
    print("Binary Search Result:", binary_search(arr, target))
