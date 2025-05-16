import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

# Function to fetch medicine names based on input
def fetch_medicine_names(event=None):
    try:
        # Get the typed text
        #typed_text = medicine_entry.get().strip().lower()
        
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="pharm"
        )
        cursor = conn.cursor()

        # Query the database for medicine names based on typed text
        cursor.execute("SELECT medname FROM medicine WHERE LOWER(medname) LIKE %s", (f'%{typed_text}%',))
        result = cursor.fetchall()

        # Update the combobox with fetched medicine names
        medicine_combobox['values'] = [row[0] for row in result]

        # Close the database connection
        conn.close()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error connecting to MySQL: {e}")

# Function to check medicine availability
def check_availability():

        # Get selected medicine name
        medicine_name = medicine_combobox.get()
        
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="pharm"
        )
        cursor = conn.cursor()

        # Query the database for the selected medicine
        cursor.execute("SELECT quant FROM medicine WHERE medname=%s", (medicine_name,))
        result = cursor.fetchone()
        
        if result:
            quantity_available = result[0]
            required_quantity = int(quantity_entry.get())
            
            if quantity_available >= required_quantity:
                messagebox.showinfo("Availability", f"{medicine_name} is available!")
            else:
                messagebox.showinfo("Availability", f"{medicine_name} is not available in required quantity.")
        else:
            messagebox.showinfo("Availability", f"{medicine_name} is not available.")

        # Close the database connection
    
# Create main window
root = tk.Tk()
root.title("Medicine Availability Checker")

# Create and place widgets
medicine_label = tk.Label(root, text="Enter medicine name:")
medicine_label.pack()

# Create a Combobox for medicine names
medicine_combobox = ttk.Combobox(root, font=("Arial", 12), width=30)
medicine_combobox.pack()

# Bind a function to update medicine names when the user types
medicine_combobox.bind("<KeyRelease>", fetch_medicine_names)

quantity_label = tk.Label(root, text="Enter required quantity:")
quantity_label.pack()

quantity_entry = tk.Entry(root)
quantity_entry.pack()

check_button = tk.Button(root, text="Check Availability", command=check_availability)
check_button.pack()

# Run the application
root.mainloop()