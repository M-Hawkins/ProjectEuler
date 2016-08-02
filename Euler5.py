def main():
    num = 2520
    flag = True

    while True:
        num += 1
        for div in range(1, 20):
            if num % div != 0:
                flag = False
                break
        if flag:
            return num
        else:
            flag = True

print(main())
