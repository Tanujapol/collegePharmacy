import tkinter as tk
from tkinter import messagebox
import mysql.connector

def update_stock():
    # Get values from entry widgets
    medicine_name = medicine_name_entry.get()
    quantity_to_add = quantity_entry.get()

    if not medicine_name :
        messagebox.showerror("Error", "Please fill in  Medicine Name to Add.")
        return
    if  not quantity_to_add:
        messagebox.showerror("Error", "Please fill in  Quantity to Add.")
        return
    if not medicine_name and not quantity_to_add:
        messagebox.showerror("Error", "Please fill in  Medicine Name and Quantity to Add.")
        return

    try:
        quantity_to_add = int(quantity_to_add)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be a valid integer.")
        return

    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",  # Change to your host
        user="root",  # Change to your username
        passwd="root",  # Change to your password
        database="pharm"  # Change to your database name
    )
    cursor = db.cursor()

    # Fetch current quantity from the database
    cursor.execute("SELECT quant FROM medicine WHERE medname = %s", (medicine_name,))
    result = cursor.fetchone()

    if result:
        current_quantity = result[0]
        new_quantity = current_quantity + quantity_to_add

        # Update stock in the database
        cursor.execute("UPDATE medicine SET quant = %s WHERE medname = %s", (new_quantity, medicine_name))
        db.commit()

        messagebox.showinfo("Success", f"Stock updated successfully. New quantity for {medicine_name}: {new_quantity}")
    else:
        messagebox.showerror("Error", f"Medicine '{medicine_name}' not found in the database")

    # Close the database connection
    db.close()

# Create a tkinter window
window = tk.Tk()
window.title("Update Stock")

# Create labels and entries for medicine name and quantity
medicine_name_label = tk.Label(window, text="Medicine Name:", font=("Arial", 14))
medicine_name_label.grid(row=0, column=0, padx=10, pady=10)

medicine_name_entry = tk.Entry(window, font=("Arial", 14))
medicine_name_entry.grid(row=0, column=1, padx=10, pady=10)

quantity_label = tk.Label(window, text="Quantity to Add:", font=("Arial", 14))
quantity_label.grid(row=1, column=0, padx=10, pady=10)

quantity_entry = tk.Entry(window, font=("Arial", 14))
quantity_entry.grid(row=1, column=1, padx=10, pady=10)

# Create button to update stock
update_button = tk.Button(window, text="Update Stock", font=("Arial", 14), command=update_stock)
update_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the tkinter event loop
window.mainloop()