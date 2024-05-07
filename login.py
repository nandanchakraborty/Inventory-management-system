from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib
import time

from main_dashboard import InventoryManagementSystem
from bill import BillClass


class LoginSystem:
    def __init__(self, root):
        self.lbl_change_image = None
        self.root = root

        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        self.otp = ''
        # ----------------image---------------------

        self.phone_image = ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_phone_image = Label(self.root, image=self.phone_image, bd=0).place(x=250, y=50)

        # Left image
         # ----------------login frame---------------------
        self.employee_id = StringVar()
        self.password = StringVar()

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="#CD853F")
        login_frame.place(x=680, y=90, width=350, height=460)

        title = Label(login_frame, text="Login System", font=("Elephant", 30, "bold"), bg="#CD853F").place(x=0, y=30,
                                                                                                           relwidth=1)

        lbl_user = Label(login_frame, text="Employee ID", font=("Andalus", 15), bg="#CD853F").place(x=50, y=100)
        txt_employee_id = Entry(login_frame, textvariable=self.employee_id, font=("times new roman", 15),
                                bg="#ECECEC").place(x=50, y=140, width=250)

        lbl_pass = Label(login_frame, text="Password", font=("Andalus", 15), bg="#CD853F").place(x=50, y=200)
        txt_pass = Entry(login_frame, font=("times new roman", 15), show="*", textvariable=self.password,
                         bg="#ECECEC").place(x=50, y=240, width=250)

        btn_login = Button(login_frame, command=self.login, text="Log In", font=("Ariel Rounded MT Bold", 15),
                           bg="#00B0F0", activebackground="#00B0F0", fg="white", activeforeground="white",
                           cursor="hand2").place(x=50, y=300, width=250, height=35)

        hr = Label(login_frame, bg="lightgray").place(x=50, y=370, width=250, height=2)
        or_ = Label(login_frame, text="OR", bg="white", fg="lightgray", font=("times new roman", 15, "bold")).place(
            x=150, y=355)

        btn_forget = Button(login_frame, text="Forget Password?", command=self.forget_window,
                            font=("times new roman", 13), bg="white", fg="#00759E", activebackground="white",
                            activeforeground="#00759E", bd=0, ).place(x=100, y=390)

        # -----------------------frame 2 --------------------------------
        register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="#aaa9ad")
        register_frame.place(x=680, y=550, width=350, height=80)

        lbl_reg = Label(register_frame, text="BUBT HARDWARE", font=("times new roman", 13), bg="#aaa9ad").place(x=100,
                                                                                                                y=20)

        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2 = ImageTk.PhotoImage(file="images/im2.png")
        self.im3 = ImageTk.PhotoImage(file="images/im3.png")
        self.lbl_change_image = Label(self.root, bg="white")
        self.lbl_change_image.place(x=420, y=153, width=240, height=428)
        self.animate()



    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3 =self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
        
        

    def login(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password.get() == "":
                messagebox.showerror('Error', "All Fields are Required", parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass=?",
                            (self.employee_id.get(), self.password.get()))
                user = cur.fetchone()
                if user is None:
                    messagebox.showerror('Error', "Invalid Username/Password", parent=self.root)
                else:
                    # print(user)
                    if user[0] == "Admin":
                        self.root.destroy()
                        self.open_admin_dashboard()
                    elif user[0] == "Employee":
                        self.root.destroy()
                        self.open_bill_dashboard()

                        # os.system("python bill.py")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def open_admin_dashboard(self):
        r = Tk()
        InventoryManagementSystem(r)
        r.mainloop()

    def open_bill_dashboard(self):
        r = Tk()
        BillClass(r)
        r.mainloop()
    def is_logged_in(self):
        return self.logged_in

    def get_user_type(self):
        return self.user_type

    def forget_window(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "":
                messagebox.showerror('Error', "Employ ID must be Required", parent=self.root)
            else:
                cur.execute("select email from employee where eid=?", (self.employee_id.get(),))
                email = cur.fetchone()
                if email == None:
                    messagebox.showerror('Error', "Invalid Employee ID, Try Again", parent=self.root)
                else:
                    # --------------forget window--------------
                    self.var_otp = StringVar()
                    self.var_new_passw = StringVar()
                    self.var_conf_passw = StringVar()

                    chk = self.send_email(email[0])
                    if chk == 'f':
                        messagebox.showerror("Error", "Connection Error , Try Again", parent=self.root)
                    else:
                        self.forget_win = Toplevel(self.root)
                        self.forget_win.title('Reset Password')
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()

                        title = Label(self.forget_win, text="Reset Password", font=('goudy old style', 15, 'bold'),
                                      bg="#3f51b5", fg="white").pack(side=TOP, fill=X)
                        lbl_reset = Label(self.forget_win, text="Enter OTP sent of Registered Email",
                                          font=('times new roman', 15)).place(x=20, y=60)
                        txt_reset = Entry(self.forget_win, textvariable=self.var_otp, font=('times new roman', 15),
                                          bg="lightyellow").place(x=20, y=100, width=250, height=30)
                        self.btn_reset = Button(self.forget_win, text="SUBMIT", command=self.validate_otp,
                                                font=("times new roman", 15), bg="lightblue")
                        self.btn_reset.place(x=280, y=100, width=100, height=30)

                        lbl_new_pass = Label(self.forget_win, text="New Password", font=('times new roman', 15)).place(
                            x=20, y=160)
                        txt_new_pass = Entry(self.forget_win, textvariable=self.var_new_passw,
                                             font=('times new roman', 15), bg="lightyellow").place(x=20, y=190,
                                                                                                   width=250, height=30)

                        lbl_c_pass = Label(self.forget_win, text="Confirm Password",
                                           font=('times new roman', 15)).place(x=20, y=225)
                        txt_c_pass = Entry(self.forget_win, textvariable=self.var_conf_passw,
                                           font=('times new roman', 15), bg="lightyellow").place(x=20, y=255, width=250,
                                                                                                 height=30)

                        self.btn_update = Button(self.forget_win, text="Update", command=self.update_password,state=DISABLED,
                                                 font=("times new roman", 15), bg="lightblue")
                        self.btn_update.place(x=150, y=300, width=100, height=30)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def update_password(self):
        if self.var_new_passw.get() == "" or self.var_conf_passw.get() == "":
            messagebox.showerror("Error", "Password is Required", parent=self.forget_win)
        elif self.var_new_passw.get() != self.var_conf_passw.get():
            messagebox.showerror("Error", "Password do not match", parent=self.forget_win)
        else:
            con = sqlite3.connect(database=r'ims.db')
            cur = con.cursor()
            try:
                cur.execute("Update employee SET pass=? where eid=?",
                            (self.var_new_passw.get(), self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password updated successfully",parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def validate_otp(self):
        if int(self.otp) == int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error", "Invalid OTP, Try again", parent=self.forget_win)

    def send_email(self, to_):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        email_ = email_pass.email_
        pass_ = email_pass.pass_

        s.login(email_, pass_)

        self.otp = int(time.strftime("%H%S%M")) + int(time.strftime("%S"))
        subj = 'IMS - Reset Password OTP'
        msg = f'Dear sir /Madam,\n\nYour Reset OTP is {str(self.otp)}. \n\nWith Regards, \nIMS Team'
        msg = "Subject: {}\n\n{}".format(subj, msg)
        s.sendmail(email_, to_, msg)
        chk = s.ehlo()
        if chk[0] == 250:
            return 's'
        else:
            return 'f'


root = Tk()
obj = LoginSystem(root)
root.mainloop()
