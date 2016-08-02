def longestCollatzSequence(top):
    ans = -1
    lChain = -1
    for num in range(top):
        n = num
        chain = 1
        while n > 1:
            if n % 2 == 0: n /= 2
            else: n = 3 * n + 1
            chain += 1
        # print(str(num) + ": " + str(chain))
        if chain > lChain:
            lChain = chain
            ans = num
    return ans

print(longestCollatzSequence(1000000))
