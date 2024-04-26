from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

import sqlite3

from utils import get_db_conn

from exceptions import DeleteError


class SalesClass:
    """
    class for product
    """

    def __init__(self, r):
        employee_form_font = ("goudy old style", 20)
        self.root = r
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_invoice = StringVar()

        # title==============

        lbl_title = (Label(self.root, text="Customer Bill View",
                           font=employee_form_font, bg="#184a45",
                           fg="white", bd=3, relief=RIDGE)
                     .pack(side=TOP, fill=X, padx=10, pady=20))
        lbl_invoice = (Label(self.root, text="Invoice No.", font=("times new roman", 15), bg="white")
                       .place(x=50, y=100))
        txt_invoice = (Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 15), bg="lightyellow")
                       .place(x=160, y=100, width=180, height=28))
        btn_search = (Button(self.root, text="Search", font=("times new roman", 15, "bold"), bg="#2196fc", fg="white",
                             cursor="hand2")
                      .place(x=360, y=100, width=120, height=28))
        btn_clear = (Button(self.root, text="Clear", font=("times new roman", 15, "bold"), bg="lightgray",
                            cursor="hand2")
                     .place(x=490, y=100, width=120, height=28))
        # bill list
        sales_Frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_Frame.place(x=50, y=140, width=200, height=330)
        scrolly = Scrollbar(sales_Frame, orient=VERTICAL)
        self.sales_list = Listbox(sales_Frame, font=("goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH, expand=1)
        # bill area
        bill_Frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_Frame.place(x=280, y=140, width=410, height=330)

        lbl_title2 = (Label(bill_Frame, text="Customer Bill Area",
                            font=employee_form_font, bg="orange"
                            )
                      .pack(side=TOP, fill=X))

        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area = Text(bill_Frame, font=("goudy old style", 15), bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

        # image=======
        self.bill_photo = Image.open("images/cat2.jpg")
        self.bill_photo = self.bill_photo.resize((450, 300), Image.LANCZOS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)

        lbl_image = Label(self.root, image=self.bill_photo, bd=0)
        lbl_image.place(x=700, y=110)


if __name__ == "__main__":
    root = Tk()
    obj = SalesClass(root)
    root.mainloop()
