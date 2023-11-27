for i in range(10):
    for j in range(i + 1, 10):
        combination = i * 10 + j
        print("{:02}, ".format(combination), end="" if j < 9 else "\n")
