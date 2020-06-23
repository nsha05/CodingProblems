r1 = int(input())
r2 = int(input())
r3 = int(input())
r4 = int(input())

if r1 < r2 and r2 < r3 and r3 < r4:
    print("Fish Rising")
elif r1 > r2 and r2 > r3 and r3 > r4:
    print("Fish Diving")
elif r1 == r2 and r2 == r3 and r3 == r4:
    print("Constant Depth")
else:
    print("No Fish")