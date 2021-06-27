# arranging widgets by placing at xy coordinates

import tkinter as tk

root = tk.Tk()
root.geometry('300x200')
root.resizable(True, True)
root.title('Tkinter place Geometry Manager')
root.wm_minsize(300, 200)

# label 1
label1 = tk.Label(
    root,
    text="Absolute Placement",
    bg='red',
    fg='white'
)

label1.place(x=20, y=20)

# label2
label2 = tk.Label(
    root,
    text="Relative placement",
    bg='blue',
    fg='white'
)

label2.place(relx=0.8, rely=0.2, relwidth=0.5, anchor='ne')

root.mainloop()
