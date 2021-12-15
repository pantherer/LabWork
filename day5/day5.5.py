#reversing the number
num = int(input("enter the number"))
new= 0
while num != 0:
    rev = num % 10
    new = new * 10 + rev
    num = num // 10
print(new)