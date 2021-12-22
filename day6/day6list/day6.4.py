a = [1,3,4,2,4,5,6]
smallest = a[0]

for i in range (len(a)-1):


    if a[i+1] < smallest:
        smallest = a[i+1]

print("the smallest number is ",smallest)