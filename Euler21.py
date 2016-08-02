def d(num):
    divs = []
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            divs += [i]
    return sum(divs)

def amicableNumbers(topNum):
    ans = 0
    for i in range(topNum):
        temp = d(i)
        if d(temp) == i and temp != i:
            ans += i
    return ans

print(amicableNumbers(10000))
