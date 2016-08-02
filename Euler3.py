def listPrimeFactors(num):
    factors = []
    div = 2
    while num > 1:
        while num % div == 0:
            factors.append(div)
            num /= div
        div += 1
        if div * div > num:
            if num > 1:
                factors.append(num)
                break
    return factors

print(max(listPrimeFactors(600851475143)))
