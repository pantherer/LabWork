'''a =["a","e","i","o","u"]
c =(input("enter any character"))
if c == (a[0] or [1] or a[2] or a[3] or a[4]):
    print("vowel")
else:
    print("not vowel")'''

#fifth question
number = int(input("enter the number"))
num = 1
count = 0

while num <= number:
    while ((number % num) == 0):
        count = count + 1
        print(count)
        break
    num = num + 1

if count == 2:
    print("it is prime ")
else:
    print("it is not prime ")

