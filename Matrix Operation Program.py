import numpy as np

# Function to get matrix input from user

def get_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    
    print(f"Enter the elements row-wise, separated by spaces:")
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Error: Number of columns doesn't match.")
            return None
        matrix.append(row)
    return np.array(matrix)

# Function for matrix addition
def matrix_addition(matrix1, matrix2):
    if matrix1.shape == matrix2.shape:
        return matrix1 + matrix2
    else:
        return "Error: Matrices must have the same dimensions for addition."

# Function for matrix subtraction
def matrix_subtraction(matrix1, matrix2):
    if matrix1.shape == matrix2.shape:
        return matrix1 - matrix2
    else:
        return "Error: Matrices must have the same dimensions for subtraction."

# Function for matrix multiplication
def matrix_multiplication(matrix1, matrix2):
    if matrix1.shape[1] == matrix2.shape[0]:
        return np.dot(matrix1, matrix2)
    else:
        return "Error: Number of columns in Matrix 1 must equal number of rows in Matrix 2."

# Function for matrix transpose
def transpose_matrix(matrix):
    return matrix.T

# Function for scalar multiplication
def scalar_multiplication(matrix, scalar):
    return matrix * scalar

# Function to display matrix in a formatted way
def display_matrix(matrix):
    if isinstance(matrix, str):  # For error messages
        print(matrix)
    else:
        for row in matrix:
            print(" ".join(map(str, row)))

# Main Program Loop
def main():
    while True:
        print("\nMatrix Operations Menu:")
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Matrix Multiplication")
        print("4. Matrix Transposition")
        print("5. Scalar Multiplication")
        print("6. Exit")
        choice = input("Select an operation (1-6): ")

        if choice == "1" or choice == "2" or choice == "3":
            print("Enter Matrix 1:")
            matrix1 = get_matrix()
            print("Enter Matrix 2:")
            matrix2 = get_matrix()

            if matrix1 is None or matrix2 is None:
                continue

            if choice == "1":
                result = matrix_addition(matrix1, matrix2)
            elif choice == "2":
                result = matrix_subtraction(matrix1, matrix2)
            elif choice == "3":
                result = matrix_multiplication(matrix1, matrix2)

            display_matrix(result)

        elif choice == "4":
            print("Enter Matrix:")
            matrix = get_matrix()
            if matrix is not None:
                result = transpose_matrix(matrix)
                display_matrix(result)

        elif choice == "5":
            print("Enter Matrix:")
            matrix = get_matrix()
            scalar = float(input("Enter scalar value: "))
            if matrix is not None:
                result = scalar_multiplication(matrix, scalar)
                display_matrix(result)

        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()