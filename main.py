

def print_matrix(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            print(matrix[y][x], end=" ")
        print("")


def create_matrix():

    matrix = []

    while True:
        matrix.append(input().split(","))
        print("Next row ? y/n")
        check = input()

        if check == "y" or check == "Y":
            print("Enter next row:")
        else:
            break
    return matrix


def multiply(matrix1, matrix2):

    # Convert matrices to int
    matrix1 = [list(map(int, i)) for i in matrix1]
    matrix2 = [list(map(int, i)) for i in matrix2]

    matrix3 = []
    temp_list = []
    temp_number = 0

    for z in range(len(matrix1)):
        for y in range(len(matrix2)):
            for x in range(len(matrix2[y])):
                temp_number += matrix1[z][x]*matrix2[x][y]
            temp_list.append(temp_number)
            temp_number = 0
        matrix3.append(temp_list)
        temp_list = []

    return matrix3


def row_checker(matrix1, matrix2):

    m1_length = len(matrix1[0])
    m2_length = len(matrix2[0])

    for y in range(len(matrix1)):
            if len(matrix1[y]) != m1_length:
                return False

    for y in range(len(matrix2)):
            if len(matrix2[y]) != m2_length:
                return False

    return True


while True:
    while True:
        print("\n\nWelcome to matrix multiplier! Enter matrix rows as "
              "comma separated lists e.g. 10,14,5,etc..."
              "\nMatrices must be in the form A*B where the amount of columns in matrix A = the amount of rows in B. "
              "\nFirst matrix row:")
        matrix_1 = create_matrix()

        print("Now for the second matrix, first row:")
        matrix_2 = create_matrix()

        # compare width v height
        width_1 = len(matrix_1[0])
        height_2 = len(matrix_2)

        if width_1 != height_2 or row_checker(matrix_1, matrix_2) is False:
            print("Your dimensions are invalid for matrix multiplication. Cannot multiply")
            print_matrix(matrix_1)
            print("with")
            print_matrix(matrix_2)
            print("Start over..")
            continue
        else:
            break

    print("Multiplying")
    print_matrix(matrix_1)
    print("with")
    print_matrix(matrix_2)

    print("Result:")
    print_matrix(multiply(matrix_1, matrix_2))

    print("Do another multiplication? y/n")
    go_again = input()

    if go_again == "Y" or go_again == "y":
        continue
    else:
        break








