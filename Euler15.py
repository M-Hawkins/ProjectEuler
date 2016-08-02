def numLatticePaths(row, col):
    #Allocate amortized storage
    amor = [[-1 for x in range(col)] for y in range(row)]

    #Fill out boundaries
    for row in range(len(amor)):
        amor[row][0] = row + 2
    for col in range(len(amor[0])):
        amor[0][col] = col + 2

    #Fill out table
    for row in range(1, len(amor)):
        for col in range(1, len(amor[0])):
            amor[row][col] = amor[row - 1][col] + amor[row][col - 1]

    #Print table
    # for row in range(len(amor)):
    #     for col in range(len(amor[0])):
    #         print(amor[row][col], end = " " * (3 - len(str(amor[row][col]))))
    #     print()

    #Return max
    return amor[-1][-1]

print(numLatticePaths(20, 20))
