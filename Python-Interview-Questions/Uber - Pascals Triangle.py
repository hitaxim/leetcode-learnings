def generate(numRows):
    triangle = []
    for row_num in range(numRows):
        # Start each row with 1s
        row = [1] * (row_num + 1)
        # Fill the middle values
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        # Add the row to the triangle
        triangle.append(row)
    return triangle
