while True:
    x = []
    y = int(input())
    if y > 2 and y < 21:
        for i in range(1, y):
            for j in range(1, y):
                if y % (i + j) == 0 and i < j:
                    x.append(i)
                    x.append(j)
    print(x)
    break
