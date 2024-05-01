import os
import sqlite3
import tempfile
import time
from tkinter import *
from tkinter import ttk, messagebox


class BillClass:
    def __init__(self, r):
        self.root = r
        self.root.geometry("1350x700+0+0")
        self.root.title("  Inventory Management System")
        self.root.config(bg="white")
        self.cart_list = []
        self.chk_print = 0

        # ---------------title----------------
        self.icon_title = PhotoImage(file="images/logo1.png")
        self.title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,
                           font=("times new roman", 40, "bold"),
                           bg="#010c48", fg="white", anchor="w", padx=20)
        self.title.place(x=0, y=0, relwidth=1, height=70)

        # --------btn logout -------------
        Button(self.root, text="Logout", command=self.logout, font=("times new roman", 15, "bold"), bg="yellow",
               cursor="hand2").place(x=1150, y=10, height=50, width=150)
        # ---------clock--------------------
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-YYYY\t\t Time: HH:MM:SS", font=("times new roman", 15, "bold"), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # ------------product frame------------------------
        self.var_search = StringVar()
        ProductFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        ProductFrame1.place(x=6, y=110, width=410, height=550)

        pTitle = (Label(ProductFrame1, text="All Products", font=("goudy old style", 20, "bold"), bg="#262626", fg="white")
                  .pack(side=TOP, fill=X))

        # --------------Product Search Frame------------------
        self.var_search = StringVar()
        ProductFrame2 = Frame(ProductFrame1, bd=2, relief=RIDGE, bg="white")
        ProductFrame2.place(x=2, y=42, width=398, height=90)

        lbl_search = (Label(ProductFrame2, text="Search Product | By Name", font=("times new roman", 15, "bold"), bg="white", fg="green")
                      .place(x=2, y=5))

        lbl_search = (Label(ProductFrame2, text="Product Name", font=("times new roman", 15, "bold"), bg="white")
                      .place(x=2, y=45))
        txt_search = (Entry(ProductFrame2, textvariable=self.var_search, font=("times new roman", 15), bg="lightyellow")
                      .place(x=128, y=47, width=150, height=22))
        btn_search = (Button(ProductFrame2, text="Search", command=self.search, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2")
                      .place(x=285, y=45, width=100, height=25))
        btn_show_all = (Button(ProductFrame2, text="Show All", command=self.show, font=("goudy old style", 15), bg="#083531", fg="white", cursor="hand2")
                        .place(x=285, y=10, width=100, height=25))

        # --------------Product Details Frame------------------
        ProductFrame3 = Frame(ProductFrame1, bd=3, relief=RIDGE)
        ProductFrame3.place(x=2, y=140, width=395, height=375)

        scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)

        self.product_Table = ttk.Treeview(ProductFrame3, columns=("pid", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid", text="PID")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("qty", text="QTY")
        self.product_Table.heading("status", text="Status")
        self.product_Table["show"] = "headings"
        self.product_Table.column("pid", width=40)
        self.product_Table.column("name", width=100)
        self.product_Table.column("price", width=100)
        self.product_Table.column("qty", width=40)
        self.product_Table.column("status", width=90)
        self.product_Table.pack(fill=BOTH, expand=1)
        self.product_Table.bind("<ButtonRelease-1>", self.get_data)

        lbl_note = (Label(ProductFrame1, text="Note: 'Enter 0 Quantity to remove product from the Cart", font=("goudy old style", 11),anchor="w", bg="white", fg="red")
                    .pack(side=BOTTOM, fill=X))

        # -----------------Product Details------------------------

        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()

        Add_CartWidgetsFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Add_CartWidgetsFrame.place(x=420, y=550, width=530, height=110)

        lbl_p_name = Label(Add_CartWidgetsFrame, text="Product Name", font=("times new roman", 15), bg="white").place(x=5, y=5)
        txt_p_name = Entry(Add_CartWidgetsFrame, textvariable=self.var_pname, font=("times new roman", 15), bg="lightyellow", state='readonly').place(x=5, y=35, width=190, height=22)

        lbl_p_price = Label(Add_CartWidgetsFrame, text="Price per Qty", font=("times new roman", 15), bg="white").place(x=230, y=5)
        txt_p_price = Entry(Add_CartWidgetsFrame, textvariable=self.var_price, font=("times new roman", 15), bg="lightyellow", state='readonly').place(x=230, y=35, width=150, height=22)

        lbl_p_qty = Label(Add_CartWidgetsFrame, text="Quantity", font=("times new roman", 15), bg="white").place(x=390, y=5)

