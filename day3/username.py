username = "123"
password = "456"
for i in range(3):
    user_name1 = input("enter user name")
    password1_ = input("enter password")
    if username == user_name1 and password == password1_:
        print("successfully logged in")
        break
    elif username != user_name1 or password != password1_:
        print("invalid credentials")
    if i==2:
        print("attempt finished")


