import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.resizable(True, True)
root.title('Label Widget Demo')
root.wm_minsize(300, 200)

# show the label here
label = ttk.Label(root, text='Label with Helvetica size 14 font', font=("Helvetica", 14))
label.pack(ipadx=10, ipady=10)

# photo
photo = tk.PhotoImage(file='poggers.png')
imageLabel = ttk.Label(
    root,
    image=photo,
    padding=5,
    text='PogChamp',
    compound='top'
)
imageLabel.pack()

root.mainloop()
