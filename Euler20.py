import math

def factorialDigitSum(num):
    sNum = str(math.factorial(num))
    return sum([int(sNum[i]) for i in range(len(sNum))])

print(factorialDigitSum(100))
