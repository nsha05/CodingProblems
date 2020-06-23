h = int(input())
max_t = int(input())

A = 1

t = 1

while A > 0 and t <= max_t:
    A = -6 * t ** 4 + h * t ** 3 + 2 * t ** 2 + t
    t += 1



if A <= 0:
    print("The balloon first touches ground at hour:")
    print(t-1)
else:
    print("The balloon does not touch ground in the given time.")
