from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Balance Check")
root.geometry("350x250")
root.resizable(height=False, width=False)
root.config(bg='grey')
amount = Label(root, text="Please Enter Amount In Your Account", bg='grey')
amount.place(x=40, y=20)
amountEnt = Entry(root)
amountEnt.place(x=80, y=60)


def calc():
    try:
        if int(amountEnt.get()) < 0:
            raise ValueError
        if int(amountEnt.get()) < 3000:
            messagebox.showerror(message="You are broke!")
        elif int(amountEnt.get()) >= 3000:
            messagebox.showinfo(message="Congratulations! You qualify to go to Greece")

    except ValueError:
        messagebox.showerror(message="Invalid Amount")


checkBtn = Button(root, text="Check Qualification", borderwidth="3", bg="salmon", command=calc)
checkBtn.place(x=80, y=100)



root.mainloop()
