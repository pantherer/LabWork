digit = int(input("enter the 3 digit number"))
sum = 0
if digit < 100 or digit > 999:
    sum = 0
while digit != 0:
    a = digit % 10
    sum = sum + a
    digit = digit // 10
print("sum is ", sum)



