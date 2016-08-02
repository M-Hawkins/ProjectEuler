def main():
    ans = 0
    fib1 = 0
    fib2 = 1
    temp = 0

    while fib2 < 4000000:
        temp = fib2
        fib2 = temp + fib1
        fib1 = temp
        if fib1 % 2 == 0:
            ans += fib1
    return ans

print(main())
