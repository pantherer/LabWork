#counting odd or even
num = int(input("enter the number"))
even = 0
odd = 0
while num != 0: 
    b = num % 10
    if (b % 2 == 0):
        even = even + 1
    else:
        odd = odd + 1
    num = num // 10

print(f"total odd count {odd} and total even count {even}")
