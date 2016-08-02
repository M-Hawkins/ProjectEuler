def maxPalindromeProduct(digits):
    ans = -1
    for num1 in range(10 ** (digits - 1), 10 ** digits):
        for num2 in range(10 ** (digits - 1), 10 ** digits):
            sav = num1 * num2
            pal = str(sav)
            while len(pal) > 1:
                if pal[0] == pal[-1]:
                    pal = pal[1:-1]
                else:
                    break
            if len(pal) < 2 and sav > ans:
                ans = sav
    return ans

print(maxPalindromeProduct(3))
