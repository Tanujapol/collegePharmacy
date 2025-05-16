import tkinter as tk
from tkinter import messagebox

def open_login_window():
    create_login_window()
    welcome_window.withdraw()

def create_login_window():
    global login_window
    login_window = tk.Toplevel(welcome_window)
    login_window.title("Login")

    username_label = tk.Label(login_window, text="Username:")
    username_label.grid(row=0, column=0, padx=5, pady=5)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = tk.Label(login_window, text="Password:")
    password_label.grid(row=1, column=0, padx=5, pady=5)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    login_button = tk.Button(login_window, text="Login", command=login)
    login_button.grid(row=2, columnspan=2, padx=5, pady=5)

    back_button = tk.Button(login_window, text="Back", command=go_back)
    back_button.grid(row=3, columnspan=2, padx=5, pady=5)

def login():
    # Perform login validation here
    # For demonstration purposes, let's just show a message
    messagebox.showinfo("Login", "Login successful!")

def go_back():
    welcome_window.deiconify()
    login_window.destroy()

def create_welcome_window():
    global welcome_window
    welcome_window = tk.Tk()
    welcome_window.title("Welcome")

    welcome_label = tk.Label(welcome_window, text="WELCOME")
    welcome_label.pack()

    login_button = tk.Button(welcome_window, text="Login", command=open_login_window)
    login_button.pack()

def main():
    create_welcome_window()
    welcome_window.mainloop()

if __name__ == "__main__":
    main()
