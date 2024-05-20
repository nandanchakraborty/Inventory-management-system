from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

from utils import get_db_conn

from exceptions import DeleteError


class ProductClass:
    """
    class for product
    """

    def __init__(self, r):
        employee_form_font = ("goudy old style", 15)
        self.root = r
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        # product_Frame.attributes("-fullscreen", True)
        #  ===========variables=========

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup()
        self.var_name = StringVar()
        self.var_qty = StringVar()
        self.var_price = StringVar()
        self.var_status = StringVar()

        # ============Frame=====
        product_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        product_Frame.place(x=10, y=10, width=450, height=482)

        # =======title======
        title = Label(product_Frame, text="Manage Product Details", font=employee_form_font, bg="#0f4d7d", fg="white")
        title.pack(side=TOP, fill=X)

        # =====label=====
        lbl_category = Label(product_Frame, text="Category", font=employee_form_font, bg="white")
        lbl_category.place(x=30, y=60)
        lbl_supplier = Label(product_Frame, text="Supplier", font=employee_form_font, bg="white")
        lbl_supplier.place(x=30, y=110)
        lbl_product_name = Label(product_Frame, text="Name", font=employee_form_font, bg="white")
        lbl_product_name.place(x=30, y=160)
        lbl_price = Label(product_Frame, text="Price(P.U)", font=employee_form_font, bg="white")
        lbl_price.place(x=30, y=210)
        lbl_quantity = Label(product_Frame, text="Quantity", font=employee_form_font, bg="white")
        lbl_quantity.place(x=30, y=260)
        lbl_status = Label(product_Frame, text="Status", font=employee_form_font, bg="white")
        lbl_status.place(x=30, y=310)

        # =======option=========
        self.cmb_category = ttk.Combobox(product_Frame, textvariable=self.var_cat,
                                         values=self.cat_list, state='readonly', justify=CENTER,
                                         font=("times new roman", 15))
        self.cmb_category.place(x=150, y=60, width=200)
        self.cmb_category.current(0)
        self.cmb_supplier = ttk.Combobox(product_Frame, textvariable=self.var_sup,
                                         values=self.sup_list, state='readonly', justify=CENTER,
                                         font=("times new roman", 15))
        self.cmb_supplier.place(x=150, y=110, width=200)
        self.cmb_supplier.current(0)
        txt_name = Entry(product_Frame, textvariable=self.var_name,
                         font=("times new roman", 15), bg="lightyellow")
        txt_name.place(x=150, y=160, width=200)
        txt_price = Entry(product_Frame, textvariable=self.var_price,
                          font=("times new roman", 15), bg="lightyellow")
        txt_price.place(x=150, y=210, width=200)
        txt_quantity = Entry(product_Frame, textvariable=self.var_qty,
                             font=("times new roman", 15), bg="lightyellow")
        txt_quantity.place(x=150, y=260, width=200)
        self.cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status,
                                       values=("Active", "Inactive"), state='readonly', justify=CENTER,
                                       font=("times new roman", 15))
        self.cmb_status.place(x=150, y=310, width=200)
        self.cmb_status.current(0)

        # ========button=====

        btn_add = (Button(product_Frame, text="Save", command=self.add, font=employee_form_font, bg="#2196f3",
                          fg="white", cursor="hand2")
                   .place(x=10, y=400, width=100, height=40))
        btn_update = (Button(product_Frame, text="Update", command=self.update, font=employee_form_font, bg="#4caf50",
                             fg="white", cursor="hand2")
                      .place(x=120, y=400, width=100, height=40))
        btn_delete = (Button(product_Frame, text="Delete", command=self.delete, font=employee_form_font, bg="#f44336",
                             fg="white", cursor="hand2")
                      .place(x=230, y=400, width=100, height=40))
        btn_clear = (Button(product_Frame, text="Clear", command=self.clear_input_field, font=employee_form_font,
                            bg="#607d8b", fg="white", cursor="hand2")
                     .place(x=340, y=400, width=100, height=40))

        # ====search_frame=====
        searchFrame = LabelFrame(self.root, text="Search Product", font=("goudy old style", 12, "bold"), bd=2,
                                 relief=RIDGE, bg="white")
        searchFrame.place(x=480, y=10, width=600, height=80)
        # ==options===
        self.cmb_search = ttk.Combobox(searchFrame, textvariable=self.var_searchby,
                                       values=("Select", "Category", "Supplier", "Name"), state='readonly',
                                       justify=CENTER,
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

        # ====product_details_treeview ====

        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(p_frame, orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

        self.ProductTable = ttk.Treeview(p_frame, columns=(
            "pid", "Supplier", "Category", "Name", "Price", "qty", "status"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrollx.config(command=self.ProductTable.yview)

        self.ProductTable.heading("pid", text="Product.id")
        self.ProductTable.heading("Category", text="Category")
        self.ProductTable.heading("Supplier", text="Supplier")
        self.ProductTable.heading("Name", text="name")
        self.ProductTable.heading("Price", text="price")
        self.ProductTable.heading("qty", text="Qty")
        self.ProductTable.heading("status", text="Status")
        self.ProductTable["show"] = "headings"

        self.ProductTable.column("pid", width=90)
        self.ProductTable.column("Category", width=100)
        self.ProductTable.column("Supplier", width=100)
        self.ProductTable.column("Name", width=100)
        self.ProductTable.column("Price", width=100)
        self.ProductTable.column("qty", width=100)
        self.ProductTable.column("status", width=100)
        self.ProductTable.pack(fill=BOTH, expand=1)
        self.ProductTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    # =================================================
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con = get_db_conn()
        cur = con.cursor()
        try:
            cur.execute("select name from category")
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("select name from supplier")
            sup = cur.fetchall()
            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :  {str(ex)}", parent=self.root)

    def add(self):
        con = get_db_conn()
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Select" or self.var_cat.get() == "Empty" or self.var_sup.get() == "Select" or self.var_name.get() == "":  #can add any validation
                messagebox.showerror("Error", "All fields are  required", parent=self.root)
            else:
                cur.execute("select *from product where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Product already availabale", parent=self.root)
                else:
                    cur.execute(
                        "Insert into product( Category,Supplier,Name,Price, qty, status) "
                        "values(?,?,?,?,?,?)",
                        (
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),

                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Added Successfully", parent=self.root)
                    self.show()
                    con.close()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :  {str(ex)}", parent=self.root)
            self.show()

    def show(self):
        con = get_db_conn()
        cur = con.cursor()
        try:
            cur.execute("select *from product")
            rows = cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :  {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.ProductTable.focus()
        content = (self.ProductTable.item(f))
        row = content['values']
        # print(row)
        self.var_pid.set(row[0]),
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6]),

    def update(self):
        con = get_db_conn()
        cur = con.cursor()
        try:
            #  can add any validation
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Please select product from list", parent=self.root)
            else:

                cur.execute("select *from product where pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid product ", parent=self.root)
                else:
                    cur.execute("Update product  set Category=?,Supplier=?,name=?,\
                           price=?,qty=?,status=?\
                           where  pid=?", (
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_pid.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product  successfully updated.", parent=self.root)
                    self.show()  # show the updated table
                    self.clear_input_field()
                    con.close()

        except Exception as ex:
            messagebox.showerror("An error occurred.", parent=self.root)
            self.show()

    def delete(self):
        con = get_db_conn()
        cur = con.cursor()
        try:
            p_id = self.var_pid.get()
            if p_id == "":
                messagebox.showerror("Error", "Please select product from the list", parent=self.root)
            else:
                cur.execute("select *from product where pid=?", (p_id,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Delete Product?", parent=self.root)
                    if op:
                        cur.execute("delete from product where pid=?", (p_id,))
                        con.commit()
                        messagebox.showinfo("Delete", "Product Deleted Successfully", parent=self.root)
                        self.show()  # show the updated table
                        self.clear_input_field()
                        con.close()

        except DeleteError:
            messagebox.showerror("An error occurred.", parent=self.root)
            self.show()

    def clear_input_field(self):
        self.var_name.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.cmb_category.current(0)
        # self.txt_search.insert(END, '')
        self.cmb_supplier.current(0)
        self.cmb_status.current(0)
        self.var_pid.set('')

    def clear_search_frame(self):
        """
        method to clear search frame
        """
        self.cmb_search.current(0)
        # self.txt_search.insert(END, '')
        self.var_searchtxt.set('')

    def search(self):
        con = get_db_conn()
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Please select an option", parent=self.root)
            elif self.txt_search.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                # cur.execute(
                #     "select * from employee where " + self.var_searchby.get() + "LIKE '%" + self.var_searchtxt.get() + "%'")
                cur.execute(
                    f"""select * from product where {self.var_searchby.get()} == '{self.var_searchtxt.get()}'""")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found !!!", parent=self.root)
                self.clear_search_frame()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :  {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = ProductClass(root)
    root.mainloop()
