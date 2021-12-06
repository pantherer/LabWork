a=int(input("enter first num"))
b=int(input("enter second num"))
c=int(input("enter third num"))
smallest = a
if b < a and b < c:
    smallest = b
elif c < b and c < a:
    smallest = c
print(f"{smallest} is the smallest number")


