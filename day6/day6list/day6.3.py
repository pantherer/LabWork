a = [1,3,4,2,4,5,6]
greatest = a[1]
for i in range (len(a)-1):

    if a[i+1] > greatest:
        greatest = a[i+1]

print("the greatest number is ",greatest)