# Recursive Binary Search

# this function searches for a number in a sorted list using recursion
def binary_search(arr, target, low, high):
    # if low crosses high, the number is not in the list
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # found the number, return its position
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)  # search left half
    else:
        return binary_search(arr, target, mid + 1, high)  # search right half

# --- taking input from user ---
arr = [10, 20, 30, 40, 50]
print("List:", arr)

target = int(input("Enter the number to search: "))

result = binary_search(arr, target, 0, len(arr) - 1)

if result != -1:
    print("Number found at index", result)
else:
    print("Number not found in the list")

# Time Complexity: O(log n) - list is split in half each time
# Space Complexity: O(log n) - because of recursive function calls