import tkinter as tk
import mysql.connector
# Create a new Tkinter window
from tkinter import messagebox
from datetime import datetime
from mysql.connector import connect
from string import *
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
#window.geometry('1000x500')
window.configure(bg='lavender')

# Add heading label in the middle of frame
heading_label = tk.Label(window, text="VISHNU EDUCATIONAL SOCIETY, BHIMAVARAM", font=("Lucida Bright", 40 , "bold"), fg="crimson")
heading_label.pack(pady=20)
heading_label.place(x=200,y=15)
heading_label.config(bg='lavender')

conn = connect(
    host = 'localhost',
    user = 'root', 
    password = 'root',
    database = 'pharm'
)
cursor = conn.cursor()




'''registration2_frame = tk.Frame(window,bg="black")
registration2_frame.place(x=380, y=130, width=830, height=480)'''

def changepassword():
    
      frame4=tk.Frame(window,width=1000,height=500,bg='white')
      frame4.place(x=0,y=0)
      
      '''img4=PhotoImage(file="pass.png")
      im=Label(frame4,image=img4)
      im.pack()'''

      h1=tk.Label(frame4,text="CHANGE PASSWORD",fg='white',font=('Arial Black',30),background='navy blue')
      h1.place(x=250,y=0)

      p1=tk.Label(frame4,text="Old Password:",fg='black',bg='powder blue',font=('Arial Black',20))
      p1.place(x=150,y=100)

      #im1=PhotoImage(file="show.png")

         
      p1_entry = tk.Entry(frame4,show='*',font=('Microsoft YaHei UI Light',18,'bold'),width=20,border=2)
      p1_entry.place(x=450,y=100)
      p2=tk.Label(frame4,text="New Password:",fg='black',bg='powder blue',font=('Arial Black',20))
      p2.place(x=150,y=180)
      p2_entry =tk.Entry(frame4,show='*',font=('Microsoft YaHei UI Light',18,'bold'),width=20,border=2)
      p2_entry.place(x=450,y=180)
      p3=tk.Label(frame4,text="Confirm Password:",fg='black',bg='powder blue',font=('Arial Black',20))
      p3.place(x=150,y=260)
      p3_entry =tk.Entry(frame4,show='*',font=('Microsoft YaHei UI Light',18,'bold'),width=20,border=2)
      p3_entry.place(x=450,y=260)
      #imgb=Button(frame4,image=im1)
      #imgb.place(x=750,y=100)
      pp="pranee"

      def sub():
        if pp==p1_entry.get():
          if p2_entry.get()==p3_entry.get():
             '''update_query = "UPDATE E SET password = %s WHERE username = %s"'''
             query = 'insert into (username,password) values(%s,%s)'
             values = ("nyfa",p2_entry.get())
             cursor.execute(query,values)
             conn.commit()
             delete_query = "DELETE FROM E WHERE password = %s"
             password=pp
             cursor.execute(delete_query, (password))
             conn.commit()
             cursor.execute('select * from E;')
             '''data = cursor.fetchall()'''
             '''cursor.execute(update_query, (p2_entry.get(), "nyfa"))'''
             frame4.destroy()
            #img4.blank()
             messagebox.showinfo("Password updated","Password successfully changed!!")
          else:
            messagebox.showerror("error","confirm your password properly!!")
   
        else:
          messagebox.showerror("error","your previous password is wrong!!")

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
      show_password_checkbox =tk.Checkbutton(frame4, text="Show Passwords", variable=show_password, command=show_hide_password,font=('Cooper Black',10))
      show_password_checkbox.place(x=430,y=320)

    

      submit=tk.Button(frame4,text='UPDATE',bg='red',fg='white',font=('Cooper Black',20,'bold'),command=sub)
      submit.place(x=430,y=350)
      def back():
       frame4.destroy()
       #img4.blank()
       

      back_button=tk.Button(frame4,text='BACK',bg='white',fg='black',font=('Cooper Black',20,'bold'),command=back)
      back_button.place(x=450,y=430)


# Start the Tkinter event loop
window.mainloop()