def set_zeroes(matrix):
    
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    row_zero = [False] * rows
    col_zero = [False] * cols
    
    # First pass to find all rows and columns that need to be zeroed
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_zero[i] = True
                col_zero[j] = True
    
    # Second pass to set the elements to zero
    for i in range(rows):
        for j in range(cols):
            if row_zero[i] or col_zero[j]:
                matrix[i][j] = 0

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

set_zeroes(matrix)

for row in matrix:
    print(row)
