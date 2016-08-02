def prodPythTriplet(targetSum):
    for a in range(3, (targetSum - 3) // 3):
        for b in range(a + 1, (targetSum - a - 1) // 2):
            c = targetSum - a - b
            if c ** 2 == a ** 2 + b ** 2:
                return a * b * c

print(prodPythTriplet(1000))
