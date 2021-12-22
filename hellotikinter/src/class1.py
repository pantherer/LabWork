from tkinter import*
root = Tk()
root.geometry("400x250")
username = Label(root,text = "username").place(x=30,y=50)
e1 = Entry(root).place(x=100,y=50)
password = Label(root,text = "password").place(x=30,y=90)
e2 = Entry(root).place(x=100,y=90)
Login = Button(root,text = "login").place(x=150,y=130)
Cancel = Button(root,text = "cancel").place(x=200,y=130)
root.mainloop()



