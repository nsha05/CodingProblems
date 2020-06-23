g1 = input()
g2 = input()
g3 = input()
g4 = input()
g5 = input()
g6 = input()

total_games = g1 + g2 + g3 + g4 + g5 + g6

wins = total_games.count("W")

if wins >= 5:
    print("1")
elif wins == 3 or wins == 4:
    print("2")
elif wins == 1 or wins == 2:
    print("1")
else:
    print("-1")