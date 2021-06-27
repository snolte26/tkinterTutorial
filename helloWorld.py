import tkinter as tk

# Create the main object
root = tk.Tk()

# placing label in root window
message = tk.Label(root, text="Hello World!")
message.pack()

# Open window and keep it open until closed
root.mainloop()