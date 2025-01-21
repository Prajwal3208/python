def rotate_left(arr, k):
    k = k % len(arr)  # Handle cases where k > len(arr)
    return arr[k:] + arr[:k]

# Example
arr = [1, 2, 3, 4, 5]
rotated = rotate_left(arr, 2)
print(rotated)  # Output: [3, 4, 5, 1, 2]
