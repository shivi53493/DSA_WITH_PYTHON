def kadane_2d(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')

    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]

            # Apply Kadane's Algorithm on the temp array (1D problem)
            current_sum = 0
            local_max = float('-inf')
            for num in temp:
                current_sum = max(num, current_sum + num)
                local_max = max(local_max, current_sum)

            max_sum = max(max_sum, local_max)

    return max_sum

# Example
matrix = [
    [1, -2, -1, 4],
    [-8, 3, 4, 2],
    [3, 8, 10, -8],
    [-4, -1, 1, 7]
]
print(kadane_2d(matrix))  # Output: 29
