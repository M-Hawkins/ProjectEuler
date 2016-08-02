import os

def maxPathSum(source):
    tri = []
    f = open(source)
    for line in f:
        tri.append([int(i) for i in line.strip("\n").split(" ")])


    for row in range(len(tri) - 2, -1, -1):
        for col in range(len(tri[row])):
            tri[row][col] += max(tri[row + 1][col], tri[row + 1][col + 1])
    return tri[0][0]

    # for row in range(len(tri)):
    #     for col in range(len(tri[row])):
    #         print(tri[row][col], end=" ")
    #     print()


# for item in os.listdir():
#     print(item)
print(maxPathSum("./Python/Euler/p067_triangle.txt"))
