import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.minsize(300, 200)

def returnPressed(event):
    print('Return Key Pressed')


def log(event):
    print(event)


btn = ttk.Button(root, text='Save')
btn.bind('<Return>', returnPressed)
btn.bind('<Return>', log, add='+')

btn.focus()
btn.pack(expand=True)

root.mainloop()