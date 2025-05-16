import tkinter as tk
from tkinter import messagebox
import mysql.connector

def add_medicine_entry():
    # Create labels and entry fields for a new medicine
    row = len(med_entries) + 1

    med_name_label = tk.Label(frame, text="Medicine Name:", font=("Arial", 14), bg="skyblue")
    med_name_label.grid(row=row, column=0, padx=10, pady=10)
    med_name_entry = tk.Entry(frame)
    med_name_entry.grid(row=row, column=1, padx=10, pady=10)

    quantity_label = tk.Label(frame, text="Quantity:", font=("Arial", 14), bg="skyblue")
    quantity_label.grid(row=row, column=2, padx=10, pady=10)
    quantity_entry = tk.Entry(frame)
    quantity_entry.grid(row=row, column=3, padx=10, pady=10)

    med_entries.append((med_name_entry, quantity_entry))

    # Move the "Add Medicine" button and "Generate Bill" button down
    add_button.grid(row=row + 1, column=0, columnspan=4, pady=10)
    bill_button.grid(row=row + 2, column=0, columnspan=4, pady=10)

def generate_bill():
    # Get values from entry widgets
    total_price = 0

    for med_entry in med_entries:
        med_name = med_entry[0].get()
        quantity = med_entry[1].get()

        if med_name and quantity:
            try:
                quantity = int(quantity)

                # Connect to the database
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="root",  # Replace with your password
                    database="pharm"
                )

                cursor = connection.cursor()

                # Retrieve medicine details from the database
                cursor.execute("SELECT medname, quant, price FROM medicine WHERE medname = %s", (med_name,))
                medicine = cursor.fetchone()

                if medicine:
                    # Calculate total price
                    med_name, available_quantity, price = medicine
                    total_price += quantity * price

                    # Check if sufficient quantity is available
                    if quantity <= available_quantity:
                        # Update quantity in the database
                        updated_quantity = available_quantity - quantity
                        cursor.execute("UPDATE medicine SET quant = %s WHERE medname = %s",
                                       (updated_quantity, med_name))
                        connection.commit()
                    else:
                        messagebox.showerror("Error", f"Insufficient quantity available for {med_name}")
                        return
                else:
                    messagebox.showerror("Error", f"Medicine {med_name} not found")
                    return

            except mysql.connector.Error as error:
                messagebox.showerror("Error", f"Error connecting to the database: {error}")
                return

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        else:
            messagebox.showerror("Error", "Please fill in all fields")
            return

    # Display total bill
    messagebox.showinfo("Total Bill", f"Total Price: {total_price}")

# Create Tkinter window
window = tk.Tk()
window.title("Billing System")

# Create a frame for the billing system and place it in the center of the window
frame = tk.Frame(window)
frame.pack(pady=20)

# Create a list to store medicine entry fields
med_entries = []

# Create button to add new medicine entry fields
add_button = tk.Button(frame, text="Add Medicine", command=add_medicine_entry)

# Create button to generate bill
bill_button = tk.Button(frame, text="Generate Bill", command=generate_bill)

# Create initial labels and entry fields for a new medicine
add_medicine_entry()

# Position the buttons initially
add_button.grid(row=2, column=0, columnspan=4, pady=10)
bill_button.grid(row=3, column=0, columnspan=4, pady=10)

# Start Tkinter event loop
window.mainloop()