import math

def isPrime(num):
    if num == 1: return False
    elif num < 4: return True
    elif num % 2 == 0: return False
    elif num < 9: return True
    elif num % 3 == 0: return False
    else:
        top = math.floor(math.sqrt(num))
        i = 5
        while i <= top:
            if num % i == 0: return False
            if num % (i + 2) == 0: return False
            i += 6
        return True

def sumOfNPrimes(top):
    ans = 0
    for num in range(top):
        if isPrime(num):
            ans += num
    return ans


print(sumOfNPrimes(2000000))
