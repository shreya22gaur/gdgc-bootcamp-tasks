def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float] | int:
    """
    Calculate the dot product of a matrix and a vector.
    
    Parameters:
    - a (list of lists of int or float): The matrix.
    - b (list of int or float): The vector.
    
    Returns:
    - list of int or float: The resulting vector from the dot product.
    - int: Returns -1 if the dimensions do not match for the dot product.
    """
    # Check if dimensions are compatible
    if len(a) == 0 or len(b) == 0 or len(a[0]) != len(b):
        return -1
    
    # Compute the dot product
    c = []
    for row in a:
        # Calculate the dot product of the row with the vector
        dot_product = sum(x * y for x, y in zip(row, b))
        c.append(dot_product)
    
    return c

# Example Usage
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
vector = [7, 8, 9]

result = matrix_dot_vector(matrix, vector)
print(result)  # Output: [50, 122] or -1 if dimensions don't match