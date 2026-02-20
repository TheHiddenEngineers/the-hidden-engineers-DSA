# Day 3 - Two Pointers Technique
# Topics Covered:
# 1. When to use Two Pointers (Pattern)
# 2. Pair Sum Problem (Sorted Array)
# 3. Remove Duplicates from Sorted Array
# 4. Container With Most Water (Intro)

# --------------------------------------------------
# 1. PAIR SUM PROBLEM (SORTED ARRAY)
# --------------------------------------------------
def pair_sum(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]

        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1

    return False


# --------------------------------------------------
# 2. REMOVE DUPLICATES FROM SORTED ARRAY (IN-PLACE)
# --------------------------------------------------
def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


# --------------------------------------------------
# 3. CONTAINER WITH MOST WATER (INTRO)
# --------------------------------------------------
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# --------------------------------------------------
# MAIN EXECUTION (TESTING ALL TOPICS)
# --------------------------------------------------
if __name__ == "__main__":

    # Pair Sum
    arr = [1, 2, 4, 7, 11, 15]
    target = 15
    print("Pair Sum Exists:",
          "Yes" if pair_sum(arr, target) else "No")

    # Remove Duplicates
    nums = [1,1,2,2,3,3,3,4]
    length = remove_duplicates(nums)
    print("After Removing Duplicates:", nums[:length])

    # Container With Most Water
    height = [1,8,6,2,5,4,8,3,7]
    print("Max Water Container Area:", max_area(height))
