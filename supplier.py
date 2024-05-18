from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class SupplierClass:




    def __init__(self, r):
        employee_form_font = ("goudy old style", 15)
        self.root = r
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()



        # ====search_frame=====
        
        # ==options===
        self.lbl_search = Label(self.root, text=" Supplier ID",bg="white",
                                font=("times new roman", 15))
        self.lbl_search.place(x=580, y=80)


        self.txt_search = Entry(self.root, font=("goudy old style", 15),
                                bg="lightyellow", textvariable=self.var_searchtxt)
        self.txt_search.place(x=700, y=80)
        btn_search = Button(self.root, text="Search", command=self.search, font=employee_form_font, bg="#4caf50",
                            fg="white",
                            cursor="hand2")
        btn_search.place(x=980, y=79, width=100, height=30)
        # ====title====
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 20 ,"bold"), bg="#0f4d7d", fg="white")
        title.place(x=50, y=10, width=1000, height=40)

        # ===content===
        # ====row1=====
        lbl_supplier_invoice = Label(self.root, text="Supplier ID", font=employee_form_font, bg="white")
        lbl_supplier_invoice.place(x=50, y=80)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=employee_form_font,
                             bg="lightyellow")
        txt_supplier_invoice.place(x=180, y=80, width=180)
     ###row2========
        self.lbl_name = Label(self.root, text="Name", font=employee_form_font, bg="white")
        self.lbl_name.place(x=50, y=120)
        self.txt_name = Entry(self.root, textvariable=self.var_name, font=employee_form_font, bg="lightyellow")
        self.txt_name.place(x=180, y=120, width=180)

        # ===row3===
        lbl_contact = Label(self.root, text="Contact", font=employee_form_font, bg="white")
        lbl_contact.place(x=50, y=160)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=employee_form_font, bg="lightyellow")
        txt_contact.place(x=180, y=160, width=180)


        #===row4====
        self.lbl_desc = Label(self.root, text="Description", font=employee_form_font, bg="white")
        self.lbl_desc.place(x=50, y=200)
        self.txt_desc = Text(self.root, font=employee_form_font, bg="lightyellow")
        self.txt_desc.place(x=180, y=200, width=420, height=120)
        # ===buttons====

        btn_add = Button(self.root, text="Save", command=self.add, font=employee_form_font, bg="#2196f3",
                         fg="white", cursor="hand2").place(x=180, y=370, width=110, height=35)
        btn_update = Button(self.root, text="Update", command=self.update, font=employee_form_font, bg="#4caf50",
                            fg="white", cursor="hand2").place(x=300, y=370, width=110, height=35)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=employee_form_font, bg="#f44336",
                            fg="white", cursor="hand2").place(x=420, y=370, width=110, height=35)
        btn_clear = Button(self.root, text="Clear", command=self.clear_input_field, font=employee_form_font,
                           bg="#607d8b", fg="white", cursor="hand2").place(x=540, y=370, width=110, height=35)

        #====employee_details====
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=690, y=120, width=380, height=350)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.SupplierTable = ttk.Treeview(emp_frame, columns=(
            "invoice", "name", "contact", "desc"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrollx.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice", text="Supplier ID")
        self.SupplierTable.heading("name", text="Name")
        self.SupplierTable.heading("contact", text="Contact")
        self.SupplierTable.heading("desc", text="Description")

        self.SupplierTable["show"] = "headings"

        self.SupplierTable.column("invoice", width=90)
        self.SupplierTable.column("name", width=100)
        self.SupplierTable.column("contact", width=100)
        self.SupplierTable.column("desc", width=100)
        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    #==================================
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            elif not self.var_contact.get().startswith("01") or not self.var_contact.get().isdigit() or len(
                    self.var_contact.get()) != 11:
                messagebox.showerror("Error", "Contact number must start with '01' and contain 11 digits",
                                     parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Invoice No. already assigned, try different", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO supplier (invoice, name, contact, description) "
                        "VALUES (?, ?, ?, ?)",
                        (
                            self.var_sup_invoice.get(),
                            self.var_name.get(),
                            self.var_contact.get(),
                            self.txt_desc.get('1.0', END)
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
                    self.show()
                    self.clear_input_field()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}", parent=self.root)
        finally:
            con.close()



    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select *from supplier")
            rows = cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :  {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.SupplierTable.focus()
        content = (self.SupplierTable.item(f))
        row = content['values']
        # print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])

        self.var_contact.set(row[2])

        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END, row[3])


    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            #  can add any validation
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. Must be required", parent=self.root)

            elif not self.var_contact.get().startswith("01") or not self.var_contact.get().isdigit() or len(
                    self.var_contact.get()) != 11:
                messagebox.showerror("Error", "Contact number must start with '01' and contain 11 digits",
                                     parent=self.root)
            else:
                emp_id = self.var_sup_invoice.get()
                cur.execute("select *from supplier where invoice=?", (emp_id,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid invoice No.", parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,description=? where invoice=?", (
                        self.var_name.get(),
                        self.var_contact.get(),

                        self.txt_desc.get('1.0', END),
                        self.var_sup_invoice.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier successfully updated.", parent=self.root)
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
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No.  Must be required", parent=self.root)
            else:
                emp_id = self.var_sup_invoice.get()
                cur.execute("select *from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Delete Supplier?", parent=self.root)
                    if op == True:
                        cur.execute("delete from supplier where invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent=self.root)
                        self.show()  # show the updated table
                        self.clear_input_field()
                        con.close()


        except Exception as ex:
            messagebox.showerror("An error occured.", parent=self.root)
            self.show()

    def clear_input_field(self):
        self.var_sup_invoice.set('')
        self.var_name.set('')
        self.var_contact.set('')
        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END, '')


    def clear_search_frame(self):
        """
        method to clear search frame
       """
        self.txt_search.insert(END, '')
        self.var_searchtxt.set('')


    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.txt_search.get() == "":
                messagebox.showerror("Error", "Invoice no. should be required", parent=self.root)
            else:
                print('-------', self.var_searchtxt.get())
                # cur.execute(
                #     "select * from employee where " + self.var_searchby.get() + "LIKE '%" + self.var_searchtxt.get() + "%'")
                cur.execute("select *  from supplier where invoice=?",(self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())

                    self.SupplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found !!!", parent=self.root)
                self.clear_search_frame()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :  {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()
