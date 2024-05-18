from datetime import datetime
from tkinter import *

from PIL import Image, ImageTk
import sqlite3
import os
from tkinter import messagebox

from employee import EmployeeClass
from supplier import SupplierClass
from Category import CategoryClass
from product import ProductClass
from sales   import SalesClass


class InventoryManagementSystem:
    """
    Base class for inventory management system
    """

    def __init__(self, r):
        self.root = r
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.new_win = None
        self.new_obj = None

        #  ====title=====
        self.icon_title = PhotoImage(file="images/logo1.png")
        self.title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,
                           font=("times new roman", 40, "bold"),
                           bg="#010c48", fg="white", anchor="w", padx=20)
        self.title.place(x=0, y=0, relwidth=1, height=70)
        #  ====btn_logout==
        self.btn_logout = Button(self.root, text="Logout", command=self.logout, font=("times new roman", 15, "bold"),
                                 bg="yellow",
                                 cursor="hand2")
        self.btn_logout.place(x=1150, y=10, height=50, width=150)
        #  ====clock===
        self.lbl_clock = Label(self.root,
                               text=" Welcome to Inventory Management System\t\tDate:\t Time: HH:MM:SS",
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        #  ===left_menu==
        self.MenuLogo = Image.open("images/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        leftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        leftMenu.place(x=0, y=102, width=200, height=565)
        lbl_menulogo = Label(leftMenu, image=self.MenuLogo)
        lbl_menulogo.pack(side=TOP, fill=X)

        # left_menu_btn===
        self.icon_side = PhotoImage(file="images/side.png")

        lbl_menu = Label(leftMenu, text="Menu", font=("times new roman", 20), bg="#009688")
        lbl_menu.pack(side=TOP, fill=X)
        btn_employee = Button(leftMenu, text="Employee", command=self.employee, image=self.icon_side, compound=LEFT,
                              padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3,
                              cursor="hand2")
        btn_employee.pack(side=TOP, fill=X)

        btn_supplier = Button(leftMenu, text="Supplier", command=self.supplier, image=self.icon_side, compound=LEFT,
                              padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3,
                              cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)
        btn_category = Button(leftMenu, text="Category", command=self.Category, image=self.icon_side, compound=LEFT,
                              padx=5, anchor="w",
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_category.pack(side=TOP, fill=X)
        btn_product = Button(leftMenu, text="Product", command=self.product, image=self.icon_side, compound=LEFT,
                             padx=5, anchor="w",
                             font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_product.pack(side=TOP, fill=X)
        btn_sales = Button(leftMenu, text="Sales", command=self.sales, image=self.icon_side, compound=LEFT, padx=5,
                           anchor="w",
                           font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_sales.pack(side=TOP, fill=X)
        btn_exit = Button(leftMenu, text="Exit", image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                          font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_exit.pack(side=TOP, fill=X)

        # ##content===
        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                                  font=("goudy old style", 20, "bold"))

        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Total Supplier\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                                  font=("goudy old style", 20, "bold"))

        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total Category\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                                  font=("goudy old style", 20, "bold"))

        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total product\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                                 font=("goudy old style", 20, "bold"))

        self.lbl_product.place(x=300, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                               font=("goudy old style", 20, "bold"))

        self.lbl_sales.place(x=650, y=300, height=150, width=300)
        self.update_content()

    def destroy_previous_window(self):
        if hasattr(self, 'new_win') and self.new_win:
            self.new_win.destroy()

    # #====================================
    def employee(self):
        self.destroy_previous_window()
        self.new_win = Toplevel(self.root)
        self.new_obj = EmployeeClass(self.new_win)

    def supplier(self):
        self.destroy_previous_window()
        self.new_win = Toplevel(self.root)
        self.new_obj = SupplierClass(self.new_win)

    def Category(self):
        self.destroy_previous_window()
        self.new_win = Toplevel(self.root)
        self.new_obj = CategoryClass(self.new_win)

    def product(self):
        self.destroy_previous_window()
        self.new_win = Toplevel(self.root)
        self.new_obj = ProductClass(self.new_win)

    def sales(self):
        self.destroy_previous_window()
        self.new_win = Toplevel(self.root)
        self.new_obj = SalesClass(self.new_win)

    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[{str(len(product))}]')

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[{str(len(supplier))}]')

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_category.config(text=f'Total Categories\n[{str(len(category))}]')

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f'Total Employees\n[{str(len(employee))}]')
            Bill = len(os.listdir('Bill'))
            self.lbl_sales.config(text=f'Total Sales\n [{str(Bill)}]')

            """
            function to update the date and time
            """
            current_date_time = datetime.now()
            current_time = current_date_time.strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
            current_date = current_date_time.strftime('%d-%m-%Y')
            self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\tDate: {current_date}\t\
             Time: {current_time}")
            self.root.after(200, self.update_content)  # Update


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")


if __name__ == "__main__":
    root = Tk()
    obj = InventoryManagementSystem(root)
    root.mainloop()
