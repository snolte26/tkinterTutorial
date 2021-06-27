import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.minsize(300, 200)

'''
# Function for button clicked
def buttonClicked():
    print('Button has been Clicked')


# Setting a button
button = ttk.Button(root, text='Click Me', command=buttonClicked)
button.pack()
'''


def select(option):
    print(option)


ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper', command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()

root.mainloop()
