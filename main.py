# IMPORTING TKINTER AND MESSAGEBOX
from tkinter import *
from tkinter import messagebox
root = Tk()

# SETTING THE TITLE FOR THE WIDGET
root.title("Authentication")

# SETTING THE SIZE
root.geometry("350x250")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='grey')

# THE HEADING OF THE WINDOW
header = Label(root, text="PLEASE ENTER LOGIN DETAILS", bg='salmon')
header.place(x=80, y=0)

# THE USERNAME LABEL, ENTRY AND PLACEMENT
username = Label(root, text="Username", bg='grey')
username.place(x=120, y=40)
userEnt = Entry(root)
userEnt.place(x=80, y=60)

# THE PASSWORD LABEL, ENTRY AND PLACEMENT
password = Label(root, text="Password", bg='grey')
password.place(x=122, y=110)
passEnt = Entry(root)
passEnt.place(x=80, y=130)




# CREATING PASSWORD AND ASSIGNING USERNAMES
user_pass = {"Vuyani": "vuya@2021", "Atheelah": "maroon17", "Ikraam": "carsthemovies", "Nathan": "blue101", "Amanda": "@manda20"}

# DEFINING A FUNCTION FOR USER SEARCH, IF THE DETAILS MATCH, YOU WILL BE SUCCESSFUL, IF NOT, YOU WILL BE UNSUCCESSFUL.
def user_search():
    if userEnt.get() in user_pass:
        if passEnt.get() == user_pass[userEnt.get()]:
            # IF THE DETAILS ARE CORRECT THE CURRENT WINDOW WILL DESTROY AND NEXT WILL OPEN
            root.destroy()
            import window_2
        else:
            messagebox.showerror(message='Login unsuccessful')
    else:
        messagebox.showerror(message='Username doesnt exist')


authBtn = Button(root, text='Login', borderwidth="3", bg="salmon", command=user_search)
authBtn.place(x=130, y=160)


# ALLOWING THE WINDOW TO RUN
root.mainloop()
