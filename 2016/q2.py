row1 = input()
row2 = input()
row3 = input()
row4 = input()

row1 = row1.split(" ")
row2 = row2.split(" ")
row3 = row3.split(" ")
row4 = row4.split(" ")

sum1 = int(row1[0]) + int(row1[1]) + int(row1[2]) + int(row1[3])
sum2 = int(row2[0]) + int(row2[1]) + int(row2[2]) + int(row2[3])
sum3 = int(row3[0]) + int(row3[1]) + int(row3[2]) + int(row3[3])
sum4 = int(row4[0]) + int(row4[1]) + int(row4[2]) + int(row4[3])

sumA = int(row1[0]) + int(row2[0]) + int(row3[0]) + int(row4[0])
sumB = int(row1[1]) + int(row2[1]) + int(row3[1]) + int(row4[1])
sumC = int(row1[2]) + int(row2[2]) + int(row3[2]) + int(row4[2])
sumD = int(row1[3]) + int(row2[3]) + int(row3[3]) + int(row4[3])

if sum1 == sum2 and sum2 == sum3 and sum3 == sum4 and sum4 == sumA and sumA == sumB and sumB == sumC and sumC == sumD:
    print("magic")
else:
    print("not magic")





