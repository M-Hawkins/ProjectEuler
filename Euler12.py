import math

def triNumWithNDivs(numDivs):
    i = 1
    num = 1
    while True:
        cnt = 0
        i += 1
        num += i
        top = math.floor(math.sqrt(num))
        for j in range(1, top + 1):
            if num % j == 0: cnt += 2
        if num == top ** 2: cnt -= 1
        if cnt >= numDivs: return num

print(triNumWithNDivs(500))
