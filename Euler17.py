def numberLetter(start, stop):
    ans = 0
    subTwenty = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]

    for num in range(start, stop):
        o = num % 10 #ones
        t = ((num % 100) - o) // 10 #tens
        h = ((num % 1000) - (t * 10) - o) // 100 #hundreds

        if h != 0:
            ans += subTwenty[h] + 7
            if t != 0 or o != 0: ans += 3
        if t < 2: ans += subTwenty[t * 10 + o]
        else: ans += tens[t] + subTwenty[o]
    return ans + 11

print(numberLetter(1, 1000))
