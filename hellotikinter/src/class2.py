from tkinter import*
root = Tk()
root.geometry("400x300")
firstName = Label(root,text = "FirstName").place(x=30,y=50)
e1 = Entry(root).place(x=130,y=50)
LastName = Label(root,text = "LastName").place(x=30,y=90)
e2 = Entry(root).place(x=130,y=90)
email = Label(root,text = "Email").place(x=30,y=130)
e3 = Entry(root).place(x=130,y=130)
password = Label(root,text = "password").place(x=30,y=170)
e4 = Entry(root).place(x=130,y=170)
ConfirmPassword = Label(root,text = "confirm Password").place(x=30,y=210)
e5 = Entry(root).place(x=130,y=210)

Login = Button(root,text = "login").place(x=150,y=250)
Cancel = Button(root,text = "cancel").place(x=200,y=250)
root.mainloop()



