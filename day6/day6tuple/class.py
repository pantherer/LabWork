'''def greater_value(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
a = greater_value(2,3,5)
print("greater value is",a)

def last_char(a):
    return a[-1]

b = input("enter the name")
c = last_char(b)
print(f"last character is {c}")'''

def function2(a,b):
    """this is a function which will calculate average of two numbers ..
    these function doesnt work for three numbers"""
    average = (a + b)/2
    # print (average)
    return average
# v = function2(5,7)
# print (v)
print(function2.__doc__)