import tkinter as tk
from tkinter import ttk

# Create the main object
root = tk.Tk()

tk.Label(root, text='Classic').pack()
ttk.Label(root, text='Themed').pack()

# Open window and keep it open until closed
root.mainloop()