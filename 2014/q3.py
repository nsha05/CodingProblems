rounds = int(input())
points_A = 100
points_D = 100
for i in range(rounds):
    rolls = input()
    rolls = rolls.split(" ")
    roll_A = int(rolls[0])
    roll_D = int(rolls[1])
    if roll_A > roll_D:
        points_D -= roll_A
    elif roll_D > roll_A:
        points_A -= roll_D
print(points_A)
print(points_D)




