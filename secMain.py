import tkinter
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Error Handling")
root.geometry("400x400")
root.config(bg="pink")

def CheckReq():
    amount = int(edtAmount.get())
    try:
        if amount < 3000:
            messagebox.showerror("Decline","Insufficient funds")
        else:
            messagebox.showinfo("you qualify", " You qualify for the Malaysia trip. Congratulations.")
    except ValueError:
        messagebox.showerror("Error", "Please insert a valid number")


lbl2 = Label(root, text="Please enter amount in your account")
lbl2.place(x=50, y=60)
edtAmount = Entry(root)
edtAmount.place(x=50, y=100)

btnCheck = Button(root, text="CHECK QUALIFICATION", bg="red" ,command=CheckReq)
btnCheck.place(x=50, y=170)

root.mainloop()
