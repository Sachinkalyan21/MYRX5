def sort_rgb_balls(arr):
    # Initialize pointers
    left, mid, right = 0, 0, len(arr) - 1
    
    while mid <= right:
        if arr[mid] == 'B':  # Place 'B' to the left
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] == 'G':  # Keep 'G' in the middle
            mid += 1
        else:  # Place 'R' to the right
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1

    return arr

# Example usage
input_array = ['R', 'G', 'B', 'G', 'G', 'R', 'B', 'B', 'G']
output_array = sort_rgb_balls(input_array)
print(output_array)
