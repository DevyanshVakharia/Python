import tkinter as tk
from tkinter import *
from tkinter import messagebox
import smtplib
import re
from GUI_project import EMS




def read_credentials():
    with open("users.txt", "r") as f:
        lines = f.readlines()
        return [line.strip().split(":") for line in lines]


def write_credentials(credentials):
    with open("users.txt", "w") as f:
        for email, password in credentials:
            f.write(f"{email}:{password}\n")


def login():
    email = email_entry.get()
    password = password_entry.get()
    credentials = read_credentials()

    if not email:
        messagebox.showerror("Error", "Please fill the email")
        return
    if not password:
        messagebox.showerror("Error", "Please fill the password")
        return


    elif [email, password] in credentials:
        messagebox.showinfo("Success", "Login successful!")
        ems = EMS()
        ems.build_gui()    
    else:
        messagebox.showerror("Error", "Invalid email or password")
        
        
        


def forgot_password():
    email = email_entry.get()
    credentials = read_credentials()
    for stored_email, stored_password in credentials:
        if stored_email == email:
            sender_email = "devyanshvakharia2510@gmail.com"
            password = "exjuohkzdxhsjqcx"
            subject = "Password of Employee Management System"
            text = f"Hello User,\n\nWe're sending you this email because you requested to know password as you have forgot it.\n\nYour password of {email} for Employee Management System is {stored_password}\n\nThank You,\nDevyansh"
            message = 'subject: {}\n\n{}'.format(subject, text)
            s = smtplib.SMTP('smtp.gmail.com', 25)
            s.starttls()
            s.login(sender_email, password)
            s.sendmail(sender_email, email, message)
            messagebox.showinfo("Password",f"Your password is successfully sent to {email}")
            return
        if not email:
            messagebox.showerror("Error", "Please fill the email")
            return
            
            
    messagebox.showerror("Error", "Invalid email")



def register():
    email = email_entry.get()
    password = password_entry.get()
    credentials = read_credentials()
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    
    for stored_email, stored_password in credentials:

        if not email:
            messagebox.showerror("Error", "Please fill the email")
            return
        if not password:
            messagebox.showerror("Error", "Please fill the password")
            return
        elif stored_email == email:
            messagebox.showerror("Error", "email already exists")
            return
        
    if (re.fullmatch(regex,email)):
        credentials.append([email, password])
        write_credentials(credentials)
        messagebox.showinfo("Success", "Registration successful!")
    else:
        messagebox.showinfo("Error", "Enter Valid Email")
        
        
        

def view():
    if password_entry.cget('show')== "*":
        password_entry.config(show='')
    else:
        password_entry.config(show="*")
    
    

root = tk.Tk()



root.title("Login System")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.configure(bg='sky blue')

entries_frame = tk.Frame(root, bg="#0ef0e8")
entries_frame.pack(side=tk.TOP, fill=tk.X)
title = tk.Label(entries_frame, text="Welcome", font=("Calibri", 30, "bold","underline",), bg="#0ef0e8", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

email_label = tk.Label(entries_frame, text="Email",font=("Calibri", 18), bg="#0ef0e8", fg="black")
email_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
email_entry = tk.Entry(entries_frame,font=("Calibri", 16), width=30)
email_entry.place(x=100,y=89)

password_label = tk.Label(entries_frame, text="Password",font=("Calibri", 18), bg="#0ef0e8", fg="black")
password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
password_entry = tk.Entry(entries_frame, show="*",font=("Calibri", 16), width=30)
password_entry.place(x=100,y=142)

register_button = tk.Button(entries_frame, text="Register", command=register,width=28, font=("Calibri", 16, "bold"), fg="black", bd=0).grid(row=4, column=0)

login_button = tk.Button(entries_frame, text="Login", command=login,width=28, font=("Calibri", 16, "bold"), fg="black", bd=0).grid(row=4, column=1)

forgot_password_button = tk.Button(entries_frame, text="Forgot Password", command=forgot_password,width=28, font=("Calibri", 16, "bold"), fg="black", bd=0).grid(row=4, column=2)

view_button = Checkbutton(entries_frame, text="O_O", command=view,width=5, font=("Calibri", 16, "bold"), fg="black")
view_button.place(x=425,y=142)



root.mainloop()

 





