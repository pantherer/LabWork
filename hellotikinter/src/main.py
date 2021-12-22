from tkinter import*
root = Tk()
root.geometry("20x10")
a = Label(root,text="User Name")
b = Label(root,text="Password")
a.grid(row=1,column=2)
b.grid(row=2,column=2)
Login = Button (root,text="button")
Login.grid(row=3,column=3)

root.mainloop()



