def namesScores(source):
    #Read file into list
    f = open(source)
    names = []
    for name in f.readline().split(","):
        names.append(name.upper().strip("\n")[1:-1])
    names.sort()

    total = 0
    for i in range(len(names)):
        subTotal = 0
        for letter in list(names[i]):
            subTotal += (ord(letter) - 64)
        # print(str(i + 1) + ": " + str(names[i]) + ", " + str(subTotal))
        total += ((i + 1) * subTotal)
    return total

print(namesScores("./Python/Euler/p022_names.txt"))
