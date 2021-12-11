total_class = int(input("enter the number of class held"))
attendance = int(input("enter the total attendance"))
total_attendance = (attendance / total_class) * 100
print("total attendance is :", total_attendance)
if total_attendance >= 75 :
    print("you are allowed to sit on the exam")
elif total_attendance < 75 :
    print("you  are not allowed to sit on the exam")




