year = int(input())

distinct = False

while distinct == False:
    year += 1
    str_year = str(year)
    set_year = set(str_year)
    if len(set_year) == len(str_year):
        distinct = True

print(year)



