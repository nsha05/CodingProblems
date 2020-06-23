n = int(input())
k = int(input())

sum = 0

for i in range(k + 1):
    sum = sum + n * 10 ** i

print(sum)
    # new_element = n * 10 ** i
    # print(new_element)