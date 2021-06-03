from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Authentication")
root.geometry("350x250")
root.resizable(height=False, width=False)
root.config(bg='grey')
header = Label(root, text="PLEASE ENTER LOGIN DETAILS", bg='salmon')
header.place(x=80, y=0)
username = Label(root, text="Username", bg='grey')
username.place(x=120, y=40)
userEnt = Entry(root)
userEnt.place(x=80, y=60)
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
            root.destroy()
            import window_2
        else:
            messagebox.showerror(message='Login unsuccessful')
    else:
        messagebox.showerror(message='Username doesnt exist')


authBtn = Button(root, text='Login', borderwidth="3", bg="salmon", command=user_search)
authBtn.place(x=130, y=160)



root.mainloop()
