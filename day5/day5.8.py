#PRINTING FIBONACCI SEQUENCE FROM 0 TO 50
a = 0
b = 50
while (b >= 0) and (b <= 50):
    print(a)
    c = a
    a = a + c
    b = b - a
print("thats it")