import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from mysql.connector import connect,Error
from string import *

# Create a new Tkinter window
window = tk.Tk()
window.title("Pharmacy Visionary")
window.resizable(False,False)
# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry(f"{screen_width}x{screen_height}+0+0")
window.configure(bg='lavender')

bg_frame=tk.Frame(window,bg="lavender")
bg_frame.place(x=0,y=90,width=1500,height=1200)

logo_image = tk.PhotoImage(file="svecwlogo.png")

logo_label = tk.Label(window, image=logo_image)
logo_label.pack(anchor="nw") # Anchor label to top left corner

# Add heading label in the middle of frame
heading_label = tk.Label(window, text="VISHNU EDUCATIONAL SOCIETY, BHIMAVARAM", font=("Lucida Bright", 30, "bold"), fg="crimson")
heading_label.pack(pady=20)
heading_label.place(x=200,y=15)
heading_label.config(bg='lavender')

#to create a subframe inside window frame
'''sub_frame=tk.Frame(window,bg="white")
sub_frame.place(x=250,y=180,width=790,height=420)'''

conn = connect(
    host = 'localhost',
    user = 'root', 
    password = 'root',
    database = 'pharm'
)
cursor = conn.cursor()

def home():
        
    def on_label_click(event):
        admin_window()

    sub_frame=tk.Frame(window,bg="white")
    sub_frame.place(x=250,y=180,width=790,height=420)

    h_bg=tk.PhotoImage(file="medicineimage.png")
    h_bg_label=tk.Label(bg_frame,image=h_bg)
    h_bg_label.place(x=0,y=0,width=1500,height=1200)

    
 #to creat a link which redirects to another window of admin
    cl_label = tk.Label(sub_frame, text="Click here to register", fg="blue", cursor="hand2",font=("Arial", 16))
    cl_label.pack(pady=10)
    cl_label.bind("<Button-1>",on_label_click)



    ''' bg_frame=tk.Frame(window,bg="white")
    bg_frame.place(x=0,y=100,width=1500,height=1200)'''

# Create a frame for user section
    user_frame = tk.Frame(sub_frame,bg="plum")
    user_frame.place(x=25, y=70, width=350, height=270)

# Create labels and entries for user section
    user_label = tk.Label(user_frame, text="User Login", font=("Arial", 16), bg="plum")
    user_label.grid(row=0, column=0, columnspan=2, pady=10)

    register_label = tk.Label(user_frame, text="Register Number", font=("Arial", 14), bg="plum")
    register_label.grid(row=1, column=0, sticky=tk.W,pady=10)

    register_entry = tk.Entry(user_frame, font=("Arial", 12))
    register_entry.grid(row=1, column=1, sticky=tk.W,pady=10)

    phone_label = tk.Label(user_frame, text="Phone Number", font=("Arial", 14), bg="plum")
    phone_label.grid(row=2, column=0, sticky=tk.W,pady=10)

    phone_entry = tk.Entry(user_frame, font=("Arial", 12))
    phone_entry.grid(row=2, column=1, sticky=tk.W,pady=10)

    def do_login():
        reg_no = register_entry.get()
        phone = phone_entry.get()
    

        cursor.execute("SELECT * FROM Userd WHERE RegNo=%s AND Phone_Number=%s",(reg_no,phone))
       
        result=cursor.fetchone()
        if(result):
             messagebox.showinfo("Login Successful", "Welcome, " + reg_no + "!")
             register_entry.delete(0,tk.END)
             phone_entry.delete(0,tk.END)
             user_page1()
        else:
             messagebox.showerror("ERROR","Invalid Register No")
             register_entry.delete(0,tk.END)
             phone_entry.delete(0,tk.END)
        cursor.commit()
        
         

# Create a button for user login
    user_button = tk.Button(user_frame, text="Login", font=("Arial", 15), bg="white",command=do_login)
    user_button.grid(row=3, column=0, columnspan=2, pady=20)



# Create a frame for pharmacist section
    pharm_frame = tk.Frame(sub_frame, bg="lightgreen")
    pharm_frame.place(x=410, y=70, width=350, height=270)


# Create labels and entries for pharmacist section
    pharm_label = tk.Label(pharm_frame, text="Pharmacist Login", font=("Arial", 16), bg="lightgreen")
    pharm_label.grid(row=0, column=0, columnspan=2, pady=10)

    pname_label = tk.Label(pharm_frame, text="UserName", font=("Arial", 14), bg="lightgreen")
    pname_label.grid(row=1, column=0, sticky=tk.W,pady=10)

    pname_entry = tk.Entry(pharm_frame, font=("Arial", 12))
    pname_entry.grid(row=1, column=1, sticky=tk.W,pady=10)

    ppassword_label = tk.Label(pharm_frame, text="Password", font=("Arial", 14), bg="lightgreen")
    ppassword_label.grid(row=2, column=0, sticky=tk.W,pady=10)

    ppassword_entry = tk.Entry(pharm_frame, font=("Arial", 12), show="*")
    ppassword_entry.grid(row=2, column=1, sticky=tk.W,pady=10)

    def validate_pharm():
        p_username = pname_entry.get()
        p_password = ppassword_entry.get()
    

        cursor.execute("SELECT * FROM Pd WHERE username=%s AND password=%s",(p_username,p_password))
       
        result=cursor.fetchone()
        if(result):
             messagebox.showinfo("Login Successful", "Welcome, " + p_username + "!")
             pname_entry.delete(0,tk.END)
             ppassword_entry.delete(0,tk.END)
             pharm1()
        else:
             messagebox.showerror("ERROR","Invalid username or password")
             pname_entry.delete(0,tk.END)
             ppassword_entry.delete(0,tk.END)
        cursor.commit()
        

             
# Create a button for pharmacist login
    pharm_button = tk.Button(pharm_frame, text="Login", font=("Arial", 15), bg="white",command=validate_pharm)
    pharm_button.grid(row=3, column=0, columnspan=3, pady=20)
    


    def admin_window():
        # Function to open the registration window
        
        h_bg.blank()
        sub_frame.destroy()

        a_bg_label=tk.Label(bg_frame,bg="lavender")
        a_bg_label.place(x=0,y=0,width=1500,height=1200)

        asub_frame=tk.Frame(window,bg="white")
        asub_frame.place(x=750,y=150,width=470,height=465)

        ad_bg=tk.PhotoImage(file="ad1.png")
        ad_bg_label=tk.Label(asub_frame,image=ad_bg)
        ad_bg_label.place(x=0,y=0,width=470,height=465)
        
        
        #validating the admin
    
        def check_valid_user():
            adname = adname_entry.get()
            adpassword = adpassword_entry.get()
        
            valid_users = {
                    "admin1": "password1",
                    "admin2": "password2",
                    "admin3": "password3"
                    }
        
            if adname in valid_users and valid_users[adname] == adpassword:
                '''welcome_window = tk.Toplevel(window)
                welcome_label = tk.Label(welcome_window, text="WELCOME")
                welcome_label.pack()'''
                asub_frame.destroy()
                ad_frame.destroy()
                ad_bg.blank()
                register_page()
            else:
                messagebox.showerror("Error", "Invalid username or password.")
                adname_entry.delete(0, tk.END)
                adpassword_entry.delete(0, tk.END)

        def go_back():
                asub_frame.destroy()
                ad_frame.destroy()
                ad_bg.blank()
                home()
        

        # Create a frame for admin section
        ad_frame = tk.Frame(window, bg="lavender")
        ad_frame.place(x=200, y=200, width=450, height=350)

        ad_label = tk.Label(ad_frame, text="Admin Login", font=("Arial", 25), bg="lavender")
        ad_label.grid(row=0, column=0, columnspan=2, pady=10)

        adname_label = tk.Label(ad_frame, text="UserName ", font=("Arial", 20), bg="lavender")
        adname_label.grid(row=1, column=0, sticky=tk.W,pady=10)

        adname_entry = tk.Entry(ad_frame, font=("Arial", 20))
        adname_entry.grid(row=1, column=1, sticky=tk.W,pady=10)

        adpassword_label = tk.Label(ad_frame, text="Password ", font=("Arial", 20), bg="lavender")
        adpassword_label.grid(row=2, column=0, sticky=tk.W,pady=10)

        adpassword_entry = tk.Entry(ad_frame, font=("Arial", 20), show="*")
        adpassword_entry.grid(row=2, column=1, sticky=tk.W,pady=10)

        # Create a button for admin login
        ad_button = tk.Button(ad_frame, text="Login", font=("Arial", 15), bg="white",command=check_valid_user)
        ad_button.grid(row=3, column=1, columnspan=3, pady=20)

        ad_back =  tk.Button(ad_frame, text="Back", font=("Arial", 15), bg="white",command=go_back)
        ad_back.grid(row=3,column=0,columnspan=3, pady=20)

    def register_page():
         '''  rsub_frame=tk.Frame(window,bg="white")
         rsub_frame.place(x=750,y=150,width=470,height=465)

         r_bg=tk.PhotoImage(file="ad1.png")
         r_bg_label=tk.Label(rsub_frame,image=r_bg)
         r_bg_label.place(x=0,y=0,width=470,height=465)'''


         # Create a frame for registration section
         r_frame = tk.Frame(window,bg="lavender")
         r_frame.place(x=180, y=120, width=700, height=480)

        # Create labels and entries for registration section
         reg_label = tk.Label(r_frame, text="Registration", font=("Arial", 35), bg="lavender")
         reg_label.grid(row=0, column=0, columnspan=1, pady=10)
         
         fname_label = tk.Label(r_frame, text="First Name", font=("Arial", 20), bg="lavender")
         fname_label.grid(row=1, column=0, sticky=tk.W,pady=5)

         fname_entry = tk.Entry(r_frame, font=("Arial", 20))
         fname_entry.grid(row=1, column=1, sticky=tk.W,pady=5)

         lname_label = tk.Label(r_frame, text="Last Name", font=("Arial", 20), bg="lavender")
         lname_label.grid(row=2, column=0, sticky=tk.W,pady=5)

         lname_entry = tk.Entry(r_frame, font=("Arial", 20))
         lname_entry.grid(row=2, column=1, sticky=tk.W,pady=5)


         phone_label = tk.Label(r_frame, text="Phone Number", font=("Arial", 20), bg="lavender")
         phone_label.grid(row=3, column=0, sticky=tk.W,pady=5)

         phone_entry = tk.Entry(r_frame, font=("Arial", 20))
         phone_entry.grid(row=3, column=1, sticky=tk.W,pady=5)

         ur_label = tk.Label(r_frame, text="Username", font=("Arial", 20), bg="lavender")
         ur_label.grid(row=4, column=0, sticky=tk.W,pady=5)

         ur_entry = tk.Entry(r_frame, font=("Arial", 20))
         ur_entry.grid(row=4, column=1, sticky=tk.W,pady=5)

         mail_label = tk.Label(r_frame, text="Email", font=("Arial", 20), bg="lavender")
         mail_label.grid(row=5, column=0, sticky=tk.W,pady=5)

         mail_entry = tk.Entry(r_frame, font=("Arial", 20))
         mail_entry.grid(row=5, column=1, sticky=tk.W,pady=5)

         pass_label = tk.Label(r_frame, text="Password", font=("Arial", 20), bg="lavender")
         pass_label.grid(row=6, column=0, sticky=tk.W,pady=5)

         pass_entry = tk.Entry(r_frame, font=("Arial", 20))
         pass_entry.grid(row=6, column=1, sticky=tk.W,pady=5)

         cpass_label = tk.Label(r_frame, text="Confirm Password", font=("Arial", 20), bg="lavender")
         cpass_label.grid(row=7, column=0, sticky=tk.W,pady=5)

         cpass_entry = tk.Entry(r_frame, font=("Arial", 20), show="*")
         cpass_entry.grid(row=7, column=1, sticky=tk.W,pady=5)

         def do_register():
              
             # Get values from the entry widgets
             fname = fname_entry.get()
             lname = lname_entry.get()
             phone = phone_entry.get()
             username = ur_entry.get()
             email = mail_entry.get()
             password = pass_entry.get()
    
             # Insert values into the database
             sql = "INSERT INTO reg (fname, lname, phone, username, email, password) VALUES (%s, %s, %s, %s, %s, %s)"
             val = (fname, lname, phone, username, email, password)
             cursor.execute(sql, val)
             conn.commit()
    
    # Close the database connection
             
             sql_e = "INSERT INTO Pd (username, password) VALUES (%s, %s)"
             val_e = (username, password)
             cursor.execute(sql_e, val_e)
             conn.commit()
    
    # Close the database connection
              
             messagebox.showinfo("Registration Successful","Registered, " + username + "!")
             fname_entry.delete(0, tk.END)
             lname_entry.delete(0, tk.END)
             phone_entry.delete(0, tk.END)
             ur_entry.delete(0, tk.END)
             mail_entry.delete(0, tk.END)
             pass_entry.delete(0, tk.END)
             cpass_entry.delete(0,tk.END)

          
         r_button = tk.Button(r_frame, text="Register", font=("Arial", 20), bg="white",command=do_register)
         r_button.grid(row=8, column=1, columnspan=1, pady=10)

         def reg_back():
              r_frame.destroy()
              admin_window()
          
         r_back =  tk.Button(r_frame, text="Back", font=("Arial", 20), bg="white",command=reg_back)
         r_back.grid(row=8,column=0,columnspan=1, pady=10)




    def user_page1():
        h_bg.blank()
        sub_frame.destroy()

        u_bg_label=tk.Label(bg_frame,bg="lavender")
        u_bg_label.place(x=0,y=0,width=1500,height=1200)
# Create a frame for registration section
        registration_frame = tk.Frame(window,bg="lavender")
        registration_frame.place(x=350, y=150, width=700, height=480)
        
# Create labels and entries for registration section
        registration = tk.Label(registration_frame, text="Check availabitily of medicine", font=("Arial", 35), bg="lavender")
        registration.grid(row=0, column=0, columnspan=2, pady=20)

        mname_label = tk.Label(registration_frame, text="Medicine Name", font=("Arial", 25), bg="lavender")
        mname_label.grid(row=1, column=0, sticky=tk.W,pady=10)

        mname_entry = tk.Entry(registration_frame, font=("Arial", 25))
        mname_entry.grid(row=1, column=1, sticky=tk.W,pady=10)

        quan_label = tk.Label(registration_frame, text="Quantity required  ", font=("Arial", 25), bg="lavender")
        quan_label.grid(row=2, column=0, sticky=tk.W,pady=10)

        quan_entry = tk.Entry(registration_frame, font=("Arial", 25))
        quan_entry.grid(row=2, column=1, sticky=tk.W,pady=10)

        def check_avail():
          
              # Get medicine name from entry widget
                medicine_name = mname_entry.get()
    

        # Query the database for the medicine
                cursor.execute("SELECT quant FROM medicine WHERE medname=%s", (medicine_name,))
                result = cursor.fetchone()
        
                if result:
                   quantity_available = result[0]
                   required_quantity = int(quan_entry.get())
            
                   if quantity_available >= required_quantity:
                         messagebox.showinfo("Availability", f"{medicine_name} is available!")
                   else:
                        messagebox.showinfo("Availability", f"{medicine_name} is not available in required quantity.")
                else:
                     messagebox.showinfo("Availability", f"{medicine_name} is not available.")
                mname_entry.delete(0, tk.END)
                quan_entry.delete(0,tk.END)
            

# Create a button  to register
        register_button = tk.Button(registration_frame, text="check", font=("Arial", 25), bg="lightcoral",command=check_avail)
        register_button.grid(row=3, column=1, columnspan=1, pady=20)

        def reg_back():
              registration_frame.destroy()
              home()
          
        r_back =  tk.Button(registration_frame, text="Back", font=("Arial", 25), bg="white",command=reg_back)
        r_back.grid(row=3,column=0,columnspan=1, pady=10)

       



    def pharm1():
         
        h_bg.blank()
        sub_frame.destroy()

        p_bg_label=tk.Label(bg_frame,bg="lavender")
        p_bg_label.place(x=0,y=0,width=1500,height=1200)

        p1_frame = tk.Frame(window,bg="lavender")
        p1_frame.place(x=20, y=130, width=400, height=480)

# Create labels and entries for registration section
        dash = tk.Label(p1_frame, text="Dashboard", font=("Arial", 35), bg="lavender")
        dash.grid(row=0, column=0, pady=20)


# Create a button  to register
        cp_button = tk.Button(p1_frame, text=" Change Password", font=("Arial", 17), bg="darkblue",fg="white",width=17,height=1)
        cp_button.grid(row=1, column=0, pady=10)

        
        p2_frame = tk.Frame(window,bg="skyblue")
        p2_frame.place(x=320, y=130, width=860, height=480)
        
        def med_av():

            p2_frame = tk.Frame(window,bg="skyblue")
            p2_frame.place(x=320, y=130, width=860, height=480)


            med = tk.Label(p2_frame, text="Check availabitily of medicine", font=("Arial", 35), bg="skyblue")
            med.grid(row=0, column=0, columnspan=2, pady=20)

            mname_label = tk.Label(p2_frame, text="Medicine Name", font=("Arial", 25), bg="skyblue")
            mname_label.grid(row=1, column=0, sticky=tk.W,pady=10)

            medname_entry = tk.Entry(p2_frame, font=("Arial", 25))
            medname_entry.grid(row=1, column=1, sticky=tk.W,pady=10)

            mquan_label = tk.Label(p2_frame, text="Quantity required  ", font=("Arial", 25), bg="skyblue")
            mquan_label.grid(row=2, column=0, sticky=tk.W,pady=10)

            mquan_entry = tk.Entry(p2_frame, font=("Arial", 25))
            mquan_entry.grid(row=2, column=1, sticky=tk.W,pady=10)


            def check_medavail():
          
              # Get medicine name from entry widget
                medicine_name = medname_entry.get()
    

        # Query the database for the medicine
                cursor.execute("SELECT quant FROM medicine WHERE medname=%s", (medicine_name,))
                result = cursor.fetchone()
        
                if result:
                   quantity_available = result[0]
                   required_quantity = int(mquan_entry.get())
            
                   if quantity_available >= required_quantity:
                         messagebox.showinfo("Availability", f"{medicine_name} is available!")
                         medname_entry.delete(0, tk.END)
                         mquan_entry.delete(0,tk.END)
                   else:
                        messagebox.showinfo("Availability", f"{medicine_name} is not available in required quantity.")
                        medname_entry.delete(0, tk.END)
                        mquan_entry.delete(0,tk.END)
                else:
                     messagebox.showinfo("Availability", f"{medicine_name} is not available.")
                     medname_entry.delete(0, tk.END)
                     mquan_entry.delete(0,tk.END)

            med_button = tk.Button(p2_frame, text="CHECK", font=("Arial", 15), bg="white",command=check_medavail,width=7,height=1)
            med_button.grid(row=3, column=1, pady=5)           
            def back():
                p2_frame.destroy()

            back_button=tk.Button(p2_frame, text="BACK", font=("Arial", 15),width=7,height=1,command=back)
            back_button.grid(row=3, column=0, pady=5)
 

            
        ma_button = tk.Button(p1_frame, text="Medicine Availability", font=("Arial", 17), bg="darkblue",fg="white",width=17,height=1,command=med_av)
        ma_button.grid(row=2, column=0, pady=5)


        us_button = tk.Button(p1_frame, text="Update Current Stock", font=("Arial", 17), bg="darkblue",fg="white",width=17,height=1)
        us_button.grid(row=3, column=0, pady=5)
        
        def u_stock():
          # p2_frame.destroy()
            
           p2_frame = tk.Frame(window,bg="skyblue")
           p2_frame.place(x=320, y=130, width=860, height=480)
             
# Create labels and entries for medicine details
           
           med1 = tk.Label(p2_frame, text="Add New Medicine", font=("Arial", 35), bg="skyblue")
           med1.grid(row=0, column=0, columnspan=2, pady=20)
           med_name_label = tk.Label(p2_frame, text="Medicine Name:", font=("Arial", 25),bg="skyblue")
           med_name_label.grid(row=1, column=0, padx=10, pady=5)
           med_name_entry = tk.Entry(p2_frame, font=("Arial", 25))
           med_name_entry.grid(row=1, column=1, padx=10, pady=5)

           new_quantity_label = tk.Label(p2_frame, text="New Quantity:", font=("Arial", 25),bg="skyblue")
           new_quantity_label.grid(row=2, column=0, padx=10, pady=5)
           new_quantity_entry = tk.Entry(p2_frame, font=("Arial", 25))
           new_quantity_entry.grid(row=2, column=1, padx=10, pady=5)

           new_price_label = tk.Label(p2_frame, text="New Price:", font=("Arial", 25),bg="skyblue")
           new_price_label.grid(row=3, column=0, padx=10, pady=5)
           new_price_entry = tk.Entry(p2_frame, font=("Arial", 25))
           new_price_entry.grid(row=3, column=1, padx=10, pady=5)
           def update_stock():
    # Get values from entry widgets
                   med_name = med_name_entry.get()
                   new_quantity = new_quantity_entry.get()
                   new_price = new_price_entry.get()

    # Check if all fields are filled
                   if not all([med_name, new_quantity, new_price]):
                       messagebox.showerror("Error", "Please fill in all the fields")
                       return

                   try:
                       new_quantity = int(new_quantity)
                       new_price = float(new_price)
                   except ValueError:
                       messagebox.showerror("Error", "Invalid quantity or price")
                       return

                   try:
                    

    

        # Check if medicine already exists in database
                    cursor.execute("SELECT * FROM medicine WHERE medname = %s", (med_name,))
                    existing_med = cursor.fetchone()

                    if existing_med:
            # Update existing medicine quantity and price
                            cursor.execute("UPDATE medicine SET quant = %s, price = %s WHERE medname = %s",
                           (new_quantity, new_price, med_name))
                            messagebox.showinfo("Success", "Stock updated successfully")
                    else:
            # Insert new medicine into database
                            cursor.execute("INSERT INTO medicine (medname, quant, price) VALUES (%s, %s, %s)",
                           (med_name, new_quantity, new_price))
                            messagebox.showinfo("Success", "New medicine added successfully")

        # Commit changes to the database
                    conn.commit()

                   except Error as err:
                      messagebox.showerror("Error", f"Database Error: {err}")


# Create a button to update stock
           update_button = tk.Button(p2_frame, text="ADD", font=("Arial", 20),command=update_stock,width=5,height=1)
           update_button.grid(row=4, column=1, pady=15)

           def back():
                p2_frame.destroy()

           back_button=tk.Button(p2_frame, text="BACK", font=("Arial", 20),width=5,height=1,command=back)
           back_button.grid(row=4, column=0, pady=15)


        am_button = tk.Button(p1_frame, text="Add New Medicine", font=("Arial", 17), bg="darkblue",fg="white",width=17,height=1,command=u_stock)
        am_button.grid(row=4, column=0, pady=5)

        def price():
              p2_frame = tk.Frame(window,bg="skyblue")
              p2_frame.place(x=320, y=130, width=860, height=480)

              med = tk.Label(p2_frame, text="Update Price", font=("Arial", 35), bg="skyblue")
              med.grid(row=0, column=0, columnspan=2, pady=20)
              medicine_name_label = tk.Label(p2_frame, text="Medicine Name:", font=("Arial", 20), bg="skyblue")
              medicine_name_label.grid(row=1, column=0, padx=10, pady=10)

              medicine_name_entry = tk.Entry(p2_frame, font=("Arial", 20))
              medicine_name_entry.grid(row=1, column=1, padx=10, pady=10)

              new_price_label = tk.Label(p2_frame, text="New Price:", font=("Arial", 20), bg="skyblue")
              new_price_label.grid(row=2, column=0, padx=10, pady=10)

              new_price_entry = tk.Entry(p2_frame, font=("Arial", 20))
              new_price_entry.grid(row=2, column=1, padx=10, pady=10)
             
              def update_price():
    
                    medicine_name = medicine_name_entry.get()
                    new_price = float(new_price_entry.get())

                    if not all([medicine_name,new_price]):
                       messagebox.showerror("Error", "Please fill in all the fields")
                       return

    # Update price in the database
                    cursor.execute("UPDATE medicine SET price = %s WHERE medname = %s", (new_price, medicine_name))
                    conn.commit()
                    messagebox.showinfo("Success", f"Price for '{medicine_name}' updated successfully.")


# Create button to update price
              update_button = tk.Button(p2_frame, text="UPDATE", font=("Arial", 17), bg="white", command=update_price,width=7,height=1)
              update_button.grid(row=3, column=1, pady=10)

              def back():
                p2_frame.destroy()

              back_button=tk.Button(p2_frame, text="BACK", font=("Arial", 17),width=7,height=1,command=back)
              back_button.grid(row=3, column=0, pady=15)
             
    

        up_button = tk.Button(p1_frame, text="Update Price", font=("Arial", 17), bg="darkblue",fg="white",width=17,height=1,command=price)
        up_button.grid(row=5, column=0, pady=5)

        def bill():
             p2_frame = tk.Frame(window,bg="skyblue")
             p2_frame.place(x=320, y=130, width=860, height=480)
 
             def add_medicine_entry():
    # Create labels and entry fields for a new medicine
              row = len(med_entries) + 1

              med_name_label = tk.Label(p2_frame, text="Medicine Name:", font=("Arial", 20), bg="skyblue")
              med_name_label.grid(row=row, column=0, padx=10, pady=10)
              med_name_entry = tk.Entry(p2_frame)
              med_name_entry.grid(row=row, column=1, padx=10, pady=10)

              quantity_label = tk.Label(p2_frame, text="Quantity:", font=("Arial", 20), bg="skyblue")
              quantity_label.grid(row=row, column=2, padx=10, pady=10)
              quantity_entry = tk.Entry(p2_frame)
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
                                            conn.commit()
                                    else:
                                          messagebox.showerror("Error", f"Insufficient quantity available for {med_name}")
                                          return
                                  else:
                                    messagebox.showerror("Error", f"Medicine {med_name} not found")
                                    return

                              except Error as error:
                                    messagebox.showerror("Error", f"Error connecting to the database: {error}")
                                    return

                        else:
                                 messagebox.showerror("Error", "Please fill in all fields")
                                 return

    # Display total bill
                   messagebox.showinfo("Total Bill", f"Total Price: {total_price}")

# Create a frame for the billing system and place it in the center of the windo

# Create a list to store medicine entry fields
             med_entries = []

# Create button to add new medicine entry fields
             add_button = tk.Button(p2_frame, text="Add Medicine", command=add_medicine_entry,width=20,height=1,font=('Arial',17))

# Create button to generate bill
             bill_button = tk.Button(p2_frame, text="Generate Bill", command=generate_bill,width=20,height=1,font=('Arial',17))

             def back():
                p2_frame.destroy()
             back1_button = tk.Button(p2_frame, text="Back", command=back,width=20,height=1,font=('Arial',17))

             
             

# Create initial labels and entry fields for a new medicine
             add_medicine_entry()

# Position the buttons initially
             add_button.grid(row=2, column=0, columnspan=4, pady=10)
             bill_button.grid(row=3, column=0, columnspan=4, pady=10)
             back1_button.grid(row=8, column=0, columnspan=4, pady=10)
             



    

        gb_button = tk.Button(p1_frame, text="Generate Bill", font=("Arial", 17), bg="darkblue",fg="white",width=17,height=1,command=bill)
        gb_button.grid(row=6, column=0, pady=5)





# Start the Tkinter event loop
home()
window.mainloop()