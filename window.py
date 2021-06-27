import tkinter as tk

# Create the main object
root = tk.Tk()

# Changing window title
root.title('Tkinter Window Demo')

'''
# Changing initial window size and location
root.geometry('600x400+50+50')
'''

"""Centering window on screen"""
windowWidth = 400
windowHeight = 300

# Get screen dimensions
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# Find center point
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)

root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')

'''
# Keeping window from being resized
root.resizable(False, False)
'''

# Setting minimum and maximum sizes
root.minsize(300, 200)
root.maxsize(700, 600)

# Setting transparency, 1=opaque 0=transparent
root.attributes('-alpha', .999999)

# Keeping window on top
root.attributes('-topmost', 1)

# Changing the window icon
root.iconbitmap('tutorialFBI.ico')

# Placing label in root window
message = tk.Label(root, text="Hello World!")
message.pack()

# Open window and keep it open until closed
root.mainloop()