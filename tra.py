import tkinter as tk
from tkinter import messagebox
import mysql.connector

def update_price():
    try:
        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",  # Change to your host
            user="root",       # Change to your username
            passwd="root",     # Change to your password
            database="pharm"  # Change to your database name
        )
        cursor = db.cursor()

        # Get values from entry widgets
        medicine_name = medicine_name_entry.get()
        new_price = float(new_price_entry.get())

        # Update price in the database
        cursor.execute("UPDATE medicine SET price = %s WHERE medname = %s", (new_price, medicine_name))
        db.commit()

        # Close the database connection
        

        messagebox.showinfo("Success", f"Price for '{medicine_name}' updated successfully.")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input for price. Please enter a valid number.")

# Create a tkinter window
window = tk.Tk()
window.title("Update Medicine Price")

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate x and y coordinates for centering the window
x = (screen_width // 2) - (400 // 2)  # Adjust 400 according to your desired width
y = (screen_height // 2) - (200 // 2)  # Adjust 200 according to your desired height

# Set window size and position it at the center of the desktop
window.geometry(f"400x200+{x}+{y}")
window.configure(bg='lavender')

# Create a frame for update price section
update_frame = tk.Frame(window, bg="lavender")
update_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create labels and entries for medicine name and new price
medicine_name_label = tk.Label(update_frame, text="Medicine Name:", font=("Arial", 14), bg="lavender")
medicine_name_label.grid(row=0, column=0, padx=10, pady=10)

medicine_name_entry = tk.Entry(update_frame, font=("Arial", 14))
medicine_name_entry.grid(row=0, column=1, padx=10, pady=10)

new_price_label = tk.Label(update_frame, text="New Price:", font=("Arial", 14), bg="lavender")
new_price_label.grid(row=1, column=0, padx=10, pady=10)

new_price_entry = tk.Entry(update_frame, font=("Arial", 14))
new_price_entry.grid(row=1, column=1, padx=10, pady=10)

# Create button to update price
update_button = tk.Button(update_frame, text="Update Price", font=("Arial", 14), bg="skyblue3", command=update_price)
update_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the tkinter event loop
window.mainloop()