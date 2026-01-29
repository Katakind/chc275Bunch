def getmin():
    while True:
        numlist = [67, 72, 9, 32, 8, 6, 7, 12, 2348437943, 59, 2023]
        for i in numlist:
            i = int(i)
        return min(numlist)

print(getmin())