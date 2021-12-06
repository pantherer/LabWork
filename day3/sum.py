num=int(input("enter any num "))
sum = 0
while (num > 0):
    digit = num % 10
    sum += digit
    num = num // 10
print("total of the digit is :",sum)
