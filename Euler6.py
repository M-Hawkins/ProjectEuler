def intSumSquareDiff(num):
    sumSquare = 0
    squareSum = 0
    for i in range(1, num + 1):
        sumSquare += (i ** 2)
        squareSum += i
    squareSum *= squareSum
    return abs(sumSquare - squareSum)

print(intSumSquareDiff(100))
