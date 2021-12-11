'''total_day = int(input("enter the number of  days of this year"))
day = total_day/4
check
while total_day == 365 or total_day == 366:
    if day % 4 == 0:
        print("it is a common year")
    else:
        print("it is a leap year")
        break'''
total_day = int(input("enter the number of  days of this year"))
if (total_day % 4 == 0) and (total_day != 100) and (total_day == 400) :
    print ("it is leap year")
else:
    print("it is common year")




