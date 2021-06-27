import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x200')
root.resizable(True, True)
root.title('Sign in')
root.wm_minsize(300, 200)

# store email and password
email = tk.StringVar()
password = tk.StringVar()


def loginClicked():
    msg = f'You Entered Email: {email.get()} and Password: {password.get()}'
    showinfo(
        title='Information',
        message=msg
    )


# Signin frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# email
emailLabel = ttk.Label(signin, text='Email: ')
emailLabel.pack(fill='x', expand=True)

emailEntry = ttk.Entry(signin, textvariable=email)
emailEntry.pack(fill='x', expand=True)
emailEntry.focus()

# password
passwordLabel = ttk.Label(signin, text='Password: ')
passwordLabel.pack(fill='x', expand=True)

passwordEntry = ttk.Entry(signin, textvariable=password, show="*")
passwordEntry.pack(fill='x', expand=True)
passwordEntry.focus()

# login button
login_button = ttk.Button(signin, text="Login", command=loginClicked)
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()
