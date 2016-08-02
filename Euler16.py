def powerDigitSum(base, exp):
    num = str(base ** exp)
    ans = [int(num[i]) for i in range(len(num))]
    return sum(ans)

print(powerDigitSum(2, 1000))
