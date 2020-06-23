k = int(input())

lines = ["*x*", " xx", "* *"]

for i in range(3):
    for x in range(k):
        for j in range(3):
            for _ in range(k):
                print(lines[i][j], end="")
        print()
