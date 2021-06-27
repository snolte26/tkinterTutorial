import tkinter as tk
from tkinter import ttk


root = tk.Tk()

# Using keyword arguments when creating the widget
'''
ttk.Label(root, text='Hi, there').pack()
'''

# Using a dictionary index after widget creation
'''
label = ttk.Label(root)
label['text'] = 'Hi, there'
label.pack()
'''

# Using the config() method with keyword attributes

label = ttk.Label(root)
label.config(text='Hi, there')
label.pack()


root.mainloop()