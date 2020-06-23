word = input()
goods = {"I", "O", "S", "H", "Z", "X", "N"}

useful = True

for i in range(len(word)):
    if word[i] not in goods:
        useful = False

if useful == True:
    print("YES")
else:
    print("NO")

