# Import tkinter module
import tkinter as tk

# Create root window
root = tk.Tk()
root.title("Login Window")
root.geometry("500x300")

# Create a frame for user section
user_frame = tk.Frame(root, bg="lightblue")
user_frame.place(relx=0.25, rely=0.1, relwidth=0.4, relheight=0.8, anchor="n")

# Create labels and entries for user section
user_label = tk.Label(user_frame, text="User Login", font=("Arial", 16), bg="lightblue")
user_label.grid(row=0, column=0, columnspan=2, pady=10)

register_label = tk.Label(user_frame, text="Register Number:", font=("Arial", 12), bg="lightblue")
register_label.grid(row=1, column=0, sticky=tk.W)

register_entry = tk.Entry(user_frame, font=("Arial", 12))
register_entry.grid(row=1, column=1, sticky=tk.W)

phone_label = tk.Label(user_frame, text="Phone Number:", font=("Arial", 12), bg="lightblue")
phone_label.grid(row=2, column=0, sticky=tk.W)

phone_entry = tk.Entry(user_frame, font=("Arial", 12))
phone_entry.grid(row=2, column=1, sticky=tk.W)

# Create a button for user login
user_button = tk.Button(user_frame, text="Login", font=("Arial", 12), bg="white")
user_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create a frame for pharmacist section
pharm_frame = tk.Frame(root, bg="lightgreen")
pharm_frame.place(relx=0.75, rely=0.1, relwidth=0.4, relheight=0.8, anchor="n")

# Create labels and entries for pharmacist section
pharm_label = tk.Label(pharm_frame, text="Pharmacist Login", font=("Arial", 16), bg="lightgreen")
pharm_label.grid(row=0, column=0, columnspan=2, pady=10)

name_label = tk.Label(pharm_frame, text="Name:", font=("Arial", 12), bg="lightgreen")
name_label.grid(row=1, column=0, sticky=tk.W)

name_entry = tk.Entry(pharm_frame, font=("Arial", 12))
name_entry.grid(row=1, column=1, sticky=tk.W)

password_label = tk.Label(pharm_frame, text="Password:", font=("Arial", 12), bg="lightgreen")
password_label.grid(row=2, column=0, sticky=tk.W)

password_entry = tk.Entry(pharm_frame, font=("Arial", 12), show="*")
password_entry.grid(row=2, column=1, sticky=tk.W)

# Create a button for pharmacist login
pharm_button = tk.Button(pharm_frame, text="Login", font=("Arial", 12), bg="white")
pharm_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
