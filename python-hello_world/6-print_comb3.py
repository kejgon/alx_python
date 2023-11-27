for i in range(10):
    for j in range(i + 1, 10):
        combination = "{:02}".format(i * 10 + j)
        print(combination, end=", " if (i != 8 or j != 9) else "")
