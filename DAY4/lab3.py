age = int(input("enter age "))
gender = input("enter gender")
if gender == "female":
    print("you can work only on urban area")
elif (gender == "male") and (age >= 20 and age <= 40):
    print("you can work anywhere ")
elif (gender == "male") and (age >= 40 and age <= 60):
    print("you can work only on urban area")
else:
    print("error")





