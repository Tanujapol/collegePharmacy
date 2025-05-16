import tkinter as tk
from tkinter import messagebox
import re

# Create a new Tkinter window
window = tk.Tk()
window.title("Pharmacy Visionary")

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate x and y coordinates for centering the window
x = (screen_width // 2) - (500 // 2)  # Adjust 500 according to your desired width
y = (screen_height // 2) - (300 // 2)  # Adjust 300 according to your desired height

# Set window size and position it at the center of the desktop
window.geometry(f"500x300+{x}+{y}")
# window.geometry('1000x500')
window.configure(bg='lavender')

# Add heading label in the middle of frame
heading_label = tk.Label(window, text="VISHNU EDUCATIONAL SOCIETY, BHIMAVARAM", font=("Lucida Bright", 40, "bold"),
                          fg="crimson")
heading_label.pack(pady=20)
heading_label.place(x=200, y=15)
heading_label.config(bg='lavender')


# Create a frame for registration section
registration_frame = tk.Frame(window, bg="lavender")
registration_frame.place(x=200, y=150, width=500, height=750)


# Create labels and entries for registration section
registration = tk.Label(registration_frame, text="Registration", font=("Arial", 35), bg="lavender")
registration.grid(row=0, column=0, columnspan=1, pady=20)

fname_label = tk.Label(registration_frame, text="First Name:", font=("Arial", 25), bg="lavender")
fname_label.grid(row=1, column=0, sticky=tk.W)

fname_entry = tk.Entry(registration_frame, font=("Arial", 25))
fname_entry.grid(row=1, column=1, sticky=tk.W)

lname_label = tk.Label(registration_frame, text="Last Name:", font=("Arial", 25), bg="lavender")
lname_label.grid(row=2, column=0, sticky=tk.W)

lname_entry = tk.Entry(registration_frame, font=("Arial", 25))
lname_entry.grid(row=2, column=1, sticky=tk.W)


phone_label = tk.Label(registration_frame, text="Phone Number:", font=("Arial", 25), bg="lavender")
phone_label.grid(row=3, column=0, sticky=tk.W)

phone_entry = tk.Entry(registration_frame, font=("Arial", 25))
phone_entry.grid(row=3, column=1, sticky=tk.W)

username_label = tk.Label(registration_frame, text="Username:", font=("Arial", 25), bg="lavender")
username_label.grid(row=4, column=0, sticky=tk.W)

username_entry = tk.Entry(registration_frame, font=("Arial", 25))
username_entry.grid(row=4, column=1, sticky=tk.W)

mail_label = tk.Label(registration_frame, text="Email:", font=("Arial", 25), bg="lavender")
mail_label.grid(row=5, column=0, sticky=tk.W)

mail_entry = tk.Entry(registration_frame, font=("Arial", 25))
mail_entry.grid(row=5, column=1, sticky=tk.W)

pass_label = tk.Label(registration_frame, text="Password:", font=("Arial", 25), bg="lavender")
pass_label.grid(row=6, column=0, sticky=tk.W)

pass_var = tk.StringVar()
pass_entry = tk.Entry(registration_frame, font=("Arial", 25), show="*", textvariable=pass_var)
pass_entry.grid(row=6, column=1, sticky=tk.W)

def show_hide_password():
        if show_password.get():
            p1_entry.config(show="")
            p2_entry.config(show="")
            p3_entry.config(show="")
        else:
           p1_entry.config(show="*")
           p2_entry.config(show="*")
           p3_entry.config(show="*")


# Create a label and an entry for the password
     # password_label = Label(root, text="Password:")
     # password_label.place()

      #password_entry = Entry(root, show="")  # Initially hiding the password with ''
      #password_entry.pack()

# Create a check button to show/hide the password
        show_password = tk.BooleanVar()
        show_password_checkbox = tk.Label(registration_frame, text="Show Passwords", variable=show_password, command=show_hide_password,font=('Cooper Black',10))
        show_password_checkbox.place(x=430,y=320)



cpass_label = tk.Label(registration_frame, text="Confirm Password:", font=("Arial", 25), bg="lavender")
cpass_label.grid(row=7, column=0, sticky=tk.W)

cpass_var = tk.StringVar()
cpass_entry = tk.Entry(registration_frame, font=("Arial", 25), show="*", textvariable=cpass_var)
cpass_entry.grid(row=7, column=1, sticky=tk.W)

def validate_email(email):
    # Regular expression for validating an email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)


def register():
    # Get values from the entry widgets
    fname = fname_entry.get()
    lname = lname_entry.get()
    phone = phone_entry.get()
    username = username_entry.get()
    email = mail_entry.get()
    password = pass_var.get()
    cpassword = cpass_var.get()

    # Check if all fields are filled
    if not all([fname, lname, phone, username, email, password, cpassword]):
        messagebox.showerror("Error", "Please fill in all the fields")
        return

    # Check if username contains spaces or capital letters
    if ' ' in username or any(char.isupper() for char in username):
        messagebox.showerror("Error", "Username should not contain spaces or capital letters")
        return

    # Check if email is valid
    if not validate_email(email):
        messagebox.showerror("Error", "Please enter a valid email address")
        return

    # Check if password and confirm password match
    if password != cpassword:
        messagebox.showerror("Error", "Passwords do not match")
        return

    # Check if phone number contains 10 digits
    if len(phone) != 10 or not phone.isdigit():
        messagebox.showerror("Error", "Phone number should contain 10 digits")
        return

    # All validations passed, proceed with registration
    # Add your database insertion code here


# Create a button to register
register_button = tk.Button(registration_frame, text="Register", font=("Arial", 25), bg="lightcoral", command=register)
register_button.grid(row=8, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
window.mainloop()