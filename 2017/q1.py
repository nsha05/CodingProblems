a = input("c1: ")
b = input("c2: ")

if int(a) > 0 and int(b) > 0:
    print("1")
elif int(a) < 0 and int(b) > 0:
    print("2")
elif int(a) < 0 and int(b) < 0:
    print("3")
else:
    print("4")