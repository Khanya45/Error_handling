import tkinter
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Error Handling")
root.geometry("400x400")
root.config(bg="pink")

def Validation(username, password, dataList):
    if username in dataList:
        if password == dataList[username]:
            return 1
        else:
            return 0
    else:
            return -1


def verify():
    user_pass = {'Khanya': 'khanya@2021', 'Nasar': 'nasar@2021', 'Lerato': 'lerato@2021', 'Amanda': 'amanda@2021'}
    x = int(Validation(edtUsername.get(), edtPwd.get(), user_pass))
    if x == 1:
        messagebox.showinfo("message", "Correct info")
        root.destroy()
        import secMain
    elif x == 0:
        messagebox.showerror("Warning", "Incorrect password")
    elif x == -1:
        messagebox.showerror("Warning", "Username doesn't exist")



lbl1 = Label(root, text="Please enter login details")
lbl1.pack()

lblUsername = Label(root, text="USERNAME")
lblUsername.place(x=50, y=60)
edtUsername = Entry(root)
edtUsername.place(x=50, y=100)

lblPwd = Label(root, text="PASSWORD")
lblPwd.place(x=50, y=170)
edtPwd = Entry(root)
edtPwd.place(x=50, y=230)

btnLogin = Button(root, text="LOGIN", bg="red", command=verify)
btnLogin.place(x=50, y=270)

root.mainloop()
