import tkinter as tk
from tkinter import messagebox

def get_screen_size():
    screen_width = tk.Tk.winfo_screenwidth(root)
    screen_height = tk.Tk.winfo_screenheight(root)
    return screen_width, screen_height

def open_frame():
    new_window = tk.Toplevel(root)
    
    screen_width, screen_height = get_screen_size()
    new_window.geometry(f'400x300+{int((screen_width-400)/2)}+{int((screen_height-300)/2)}')
    
    label = tk.Label(new_window, text="Hello, this is a new frame!")
    label.pack()

root = tk.Tk()
root.title("Python Frame Example")

button = tk.Button(root, text="Open Frame", command=open_frame)
button.pack()

root.mainloop()