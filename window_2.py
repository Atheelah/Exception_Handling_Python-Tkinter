# IMPORTING TKINTER AND MESSAGEBOX
from tkinter import *
from tkinter import messagebox
root = Tk()

# SETTING THE TITLE FOR THE WIDGET
root.title("Balance Check")

# SETTING THE SIZE
root.geometry("350x250")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='grey')

# CREATING A LABEL AND PLACING IT
amount = Label(root, text="Please Enter Amount In Your Account", bg='grey')
amount.place(x=40, y=20)

# CREATING AN ENTRY AND PLACING IT
amountEnt = Entry(root)
amountEnt.place(x=80, y=60)

# DEFINING A FUNCTION
# IF THE BANK BALANCE IS <3000 AN ERROR MESSAGE WILL SHOW (YOU ARE BROKE)
# IF THE BANK BALANCE IS >=3000 A CONGRATULATIONS MESSAGE WILL SHOW
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

# CREATING A BUTTON. THE FUNCTION IS ASSIGNED TO THE BUTTON.
checkBtn = Button(root, text="Check Qualification", borderwidth="3", bg="salmon", command=calc)
checkBtn.place(x=80, y=100)


# ALLOWING THE WINDOW TO RUN
root.mainloop()
