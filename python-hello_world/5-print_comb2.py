# for i in range(100):
#     print("{:02}".format(i), end=", " if i < 99 else "\n")

for i in range(100):
    print(f"{i:02}", end=", " if i < 99 else "\n")
