import math

coord1 = input()
coord2 = input()
elec_charge = int(input())

coord1 = coord1.split(" ")
coord2 = coord2.split(" ")

x1 = int(coord1[0])
y1 = int(coord1[1])
x2 = int(coord2[0])
y2 = int(coord2[1])

min_distance = (x1 - x2) + (y1 -y2)
min_distance = math.fabs(min_distance)

if elec_charge < min_distance:
    print("N")
else:
    diff = elec_charge - min_distance
    if diff % 2 != 0:
        print("N")
    else:
        print("Y")


# var = False

# for i in range(10):
#     possible_route = min_distance + 2 * i
#     if possible_route == elec_charge:
#         print ("Y")
#     elif possible_route > elec_charge:
#         var = False
#
# if var == False:
#     print("N")




