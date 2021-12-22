a = {1,2,3,4,5,6,"a","m"}
b = input("enter what you want to remove")
for i in range(len(a)):
    if b == a[i]:
        a.remove(a[i])
print(a)
