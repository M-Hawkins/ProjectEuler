def findNthPrime(cnt):
    num = 2
    isPrime = True
    while cnt > 0:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                isPrime = False
                break
        if isPrime:
            cnt -= 1
        else:
            isPrime = True
        num += 1
    return num - 1

print(findNthPrime(10001))
