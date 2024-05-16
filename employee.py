from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class EmployeeClass:
    """
    class for employee
    """

    def __init__(self, r):
        employee_form_font = ("goudy old style", 15)
        self.root = r
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_utype = StringVar()
        self.var_pass = StringVar()
        self.var_salary = StringVar()

        # ====search_frame=====
        searchFrame = LabelFrame(self.root, text="Search Employee", font=("goudy old style", 12, "bold"), bd=2,
                                 relief=RIDGE, bg="white")
        searchFrame.place(x=250, y=20, width=600, height=70)
        # ==options===
        self.cmb_search = ttk.Combobox(searchFrame, textvariable=self.var_searchby,
                                       values=("Select", "Email", "Name", "Contact"), state='readonly', justify=CENTER,
                                       font=("times new roman", 15))
        self.cmb_search.place(x=10, y=10, width=180)
        self.cmb_search.current(0)

        self.txt_search = Entry(searchFrame, font=("goudy old style", 15),
                                bg="lightyellow", textvariable=self.var_searchtxt)
        self.txt_search.place(x=200, y=10)
        btn_search = Button(searchFrame, text="Search", command=self.search, font=employee_form_font, bg="#4caf50",
                            fg="white",
                            cursor="hand2")
        btn_search.place(x=470, y=9, width=120, height=30)
        # ====title====
        title = Label(self.root, text="Employ Details", font=employee_form_font, bg="#0f4d7d", fg="white")
        title.place(x=50, y=100, width=1000)

        # ===content===
        # ====row1=====
        lbl_empid = Label(self.root, text="Emp ID", font=employee_form_font, bg="white")
        lbl_empid.place(x=50, y=150)
        lbl_gender = Label(self.root, text="Gender", font=employee_form_font, bg="white")
        lbl_gender.place(x=350, y=150)
        lbl_contact = Label(self.root, text="Contact", font=employee_form_font, bg="white")
        lbl_contact.place(x=750, y=150)
        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=employee_form_font,
                          bg="lightyellow")
        txt_empid.place(x=150, y=150, width=180)
        self.cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender,
                                       values=("Select", "Male", "Female", "Other"),
                                       state='readonly', justify=CENTER, font=("times new roman", 15))
        self.cmb_gender.place(x=500, y=150, width=180)
        self.cmb_gender.current(0)
        self.txt_contact = Entry(self.root, textvariable=self.var_contact, font=employee_form_font,
                                 bg="lightyellow")
        self.txt_contact.place(x=850, y=150, width=180)

        self.lbl_name = Label(self.root, text="Name", font=employee_form_font, bg="white")
        self.lbl_name.place(x=50, y=190)
        self.lbl_dob = Label(self.root, text="D.O.B", font=employee_form_font, bg="white")
        self.lbl_dob.place(x=350, y=190)
        self.lbl_doj = Label(self.root, text="D.O.J", font=employee_form_font, bg="white")
        self.lbl_doj.place(x=750, y=190)
        self.txt_name = Entry(self.root, textvariable=self.var_name, font=employee_form_font, bg="lightyellow")
        self.txt_name.place(x=150, y=190, width=180)
        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=employee_form_font, bg="lightyellow")
        self.txt_dob.place(x=500, y=190, width=180)

        txt_doj = Entry(self.root, textvariable=self.var_doj, font=employee_form_font, bg="lightyellow")
        txt_doj.place(x=850, y=190, width=180)

        # ===row3===
        lbl_email = Label(self.root, text="Email", font=employee_form_font, bg="white")
        lbl_email.place(x=50, y=230)
        lbl_pass = Label(self.root, text="Password", font=employee_form_font, bg="white")
        lbl_pass.place(x=350, y=230)
        lbl_utype = Label(self.root, text="User Type", font=employee_form_font, bg="white")
        lbl_utype.place(x=730, y=230)
        txt_email = Entry(self.root, textvariable=self.var_email, font=employee_form_font, bg="lightyellow")
        txt_email.place(x=150, y=230, width=180)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=employee_form_font, bg="lightyellow")
        txt_pass.place(x=500, y=230, width=180)

        self.cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin", "Employee"),
                                      state='readonly',
                                      justify=CENTER, font=("times new roman", 15))
        self.cmb_utype.place(x=850, y=230, width=180)
        self.cmb_utype.current(0)

        #===row4====
        self.lbl_address = Label(self.root, text="Address", font=employee_form_font, bg="white")
        self.lbl_address.place(x=50, y=270)
        self.lbl_salary = Label(self.root, text="Salary", font=employee_form_font, bg="white")
        self.lbl_salary.place(x=500, y=270)
        self.txt_address = Text(self.root, font=employee_form_font, bg="lightyellow")
        self.txt_address.place(x=150, y=270, width=300, height=60)
        self.txt_salary = Entry(self.root, textvariable=self.var_salary, font=employee_form_font,
                                bg="lightyellow")
        self.txt_salary.place(x=600, y=270, width=180)
        # ===buttons====

        btn_add = (Button(self.root, text="Save", command=self.add, font=employee_form_font, bg="#2196f3",
                          fg="white", cursor="hand2")
                   .place(x=500, y=305, width=110, height=28))
        btn_update = (Button(self.root, text="Update", command=self.update, font=employee_form_font, bg="#4caf50",
                             fg="white", cursor="hand2")
                      .place(x=620, y=305, width=110, height=28))
        btn_delete = (Button(self.root, text="Delete", command=self.delete, font=employee_form_font, bg="#f44336",
                             fg="white", cursor="hand2")
                      .place(x=740, y=305, width=110, height=28))
        btn_clear = (Button(self.root, text="Clear", command=self.clear_input_field, font=employee_form_font,
                            bg="#607d8b", fg="white", cursor="hand2")
                     .place(x=860, y=305, width=110, height=28))

        #====employee_details====
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=(
            "eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrollx.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("eid", text="EMP ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="User type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("pass", width=100)
        self.EmployeeTable.column("utype", width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("salary", width=100)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    #==================================
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":  #can add any validation
                messagebox.showerror("Error", "Employee ID  Must be required", parent=self.root)
            elif not self.var_contact.get().startswith("01") or not self.var_contact.get().isdigit() or len(
                    self.var_contact.get()) != 11:
                messagebox.showerror("Error", "Contact number must start with '01' and contain 11 digits",
                                     parent=self.root)
            else:
                cur.execute("select *from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Id already assigned,try different", parent=self.root)
                else:
                    cur.execute(
                        "Insert into employee( eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) "
                        "values(?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Added Successfully", parent=self.root)
                    self.show()
                    con.close()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :  {str(ex)}", parent=self.root)
            self.show()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select *from employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :  {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f))
        row = content['values']
        # print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[9])

        self.var_salary.set(row[10])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            #  can add any validation
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID  Must be required", parent=self.root)

            elif not self.var_contact.get().startswith("01") or not self.var_contact.get().isdigit() or len(
                    self.var_contact.get()) != 11:
                messagebox.showerror("Error", "Contact number must start with '01' and contain 11 digits",
                                     parent=self.root)

            else:
                emp_id = self.var_emp_id.get()
                cur.execute("select *from employee where eid=?", (emp_id,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,\
                           contact=?,dob=?,doj=?,pass=?,utype=?,\
                           address=?,salary=? where eid=?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0', END),
                        self.var_salary.get(),
                        emp_id))
                    con.commit()
                    messagebox.showinfo("Success", "Employee successfully updated.", parent=self.root)
                    self.show()  # show the updated table
                    self.clear_input_field()
                    con.close()




        except Exception as ex:
            messagebox.showerror("An error occured.", parent=self.root)
            self.show()

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID  Must be required", parent=self.root)
            else:
                emp_id = self.var_emp_id.get()
                cur.execute("select *from employee where eid=?", (emp_id,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Delete Employee?", parent=self.root)
                    if op:
                        cur.execute("delete from employee where eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee Deleted Successfully", parent=self.root)
                        self.show()  # show the updated table
                        self.clear_input_field()
                        con.close()


        except Exception as ex:
            messagebox.showerror("An error occured.", parent=self.root)
            self.show()

    def clear_input_field(self):
        self.var_emp_id.set('')
        self.var_name.set('')
        self.var_email.set('')
        # self.var_gender.set('')
        self.cmb_gender.current(0)
        self.var_contact.set('')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_pass.set('')
        self.cmb_utype.current(0)
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, '')
        self.var_salary.set('')

    def clear_search_frame(self):
        """
        method to clear search frame
        """
        self.cmb_search.current(0)
        # self.txt_search.insert(END, '')
        self.var_searchtxt.set('')

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Please select an option", parent=self.root)
            elif self.txt_search.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                print('-------', self.var_searchtxt.get())
                # cur.execute(
                #     "select * from employee where " + self.var_searchby.get() + "LIKE '%" + self.var_searchtxt.get() + "%'")
                cur.execute(
                    f"""select * from employee where {self.var_searchby.get()} == '{self.var_searchtxt.get()}'""")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found !!!", parent=self.root)
                self.clear_search_frame()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :  {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = EmployeeClass(root)
    root.mainloop()
