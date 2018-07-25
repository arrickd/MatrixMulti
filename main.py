
width_1 = 0
height_2 = 0
matrix_1 = []
matrix_2 = []
matrix_3 = []
row_length = 0


def print_matrix(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            print(matrix[y][x], end=" ")
        print("")


def create_matrix(matrix):
    while True:
        matrix.append(input().split(","))
        print("Next row ? y/n")
        check = input()

        if check == "y" or check == "Y":
            print("Enter next row:")
        else:
            break


def multiply():

    temp_list = []
    temp_number = 0

    for z in range(len(matrix_2)):
        for y in range(len(matrix_1)):
            for x in range(len(matrix_1[y])):
                temp_number += matrix_1[z][x]*matrix_2[x][y]
            temp_list.append(temp_number)
            temp_number = 0
        matrix_3.append(temp_list)
        temp_list = []


go = True

while go:

    print("\n\nWelcome to matrix multiplier! Enter your matrix rows as comma separated lists e.g. 10,2,3,14,5,etc..."
          "\nFirst matrix row:")
    create_matrix(matrix_1)

    print("Matrix 1:")
    print_matrix(matrix_1)

    print("Now for the second matrix, first row:")
    create_matrix(matrix_2)

    print("Matrix 2:")
    print_matrix(matrix_2)

    matrix_1 = [list(map(int, i)) for i in matrix_1]
    matrix_2 = [list(map(int, i)) for i in matrix_2]

    multiply()

    print("Result:")
    print_matrix(matrix_3)







