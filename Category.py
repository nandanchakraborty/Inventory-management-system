from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3


class CategoryClass:


    """
    class for employee
    """

    def __init__(self, r):

        employee_form_font = ("goudy old style", 20)
        self.root = r
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        #variables=====
        self.var_cat_id=StringVar()
        self.var_name=StringVar()


#======title=========
        lbl_title = Label(self.root,text="Manage Product Category",font =employee_form_font,bg="#184a45",
        fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        lbl_name = Label(self.root,text="Enter Category Name",font=employee_form_font,bg="white").place(x=50,y=100)

        lbl_name = Entry(self.root,textvariable=self.var_name,font=employee_form_font,bg="lightyellow").place(x=50,y=150,width=300)

        btn_add= Button(self.root,text="Add",command=self.add,font=employee_form_font,bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=155,width=150,height=30)

        btn_delete= Button(self.root,text="Delete",command=self.delete,font=employee_form_font,bg="Red",fg="white",cursor="hand2").place(x=520,y=155,width=150,height=30)
  
  
   #====Category_details====
        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=690, y=80, width=380, height=110)

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.CategoryTable = ttk.Treeview(cat_frame, columns=(
            "C_id", "name"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrollx.config(command=self.CategoryTable.yview)

        self.CategoryTable.heading("C_id", text="C_id")
        self.CategoryTable.heading("name", text="Name")
        self.CategoryTable["show"] = "headings"

        self.CategoryTable.column("C_id", width=90)
        self.CategoryTable.column("name", width=100)
        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>", self.get_data)

       

#=====images=====
        self.im1=Image.open("images/cat.jpg")
        self.im1=self.im1.resize((500,250),Image.LANCZOS)
        self.im1= ImageTk.PhotoImage(self.im1)


        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RIDGE)
        self.lbl_im1.place(x=50,y=220)

        self.im2=Image.open("images/category.jpg")
        self.im2=self.im2.resize((500,250),Image.LANCZOS)
        self.im2= ImageTk.PhotoImage(self.im2)


        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RIDGE)
        self.lbl_im2.place(x=580,y=220)
        self.show()
   #===fucntion for add category====
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":  #can add any validation
                messagebox.showerror("Error", "Category must be required", parent=self.root)
            else:
                cur.execute("select *from category where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Category already availbale,try different", parent=self.root)
                else:
                    cur.execute("Insert into category(name) values(?)",
                        (
                            self.var_name.get(),


                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                    self.show()
                    self.clear_input_field()

                    con.close()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :  {str(ex)}", parent=self.root)
            self.show()





    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select *from category")
            rows = cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :  {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.CategoryTable.focus()
        content = (self.CategoryTable.item(f))
        row = content['values']
        # print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Please select or enter category from the list", parent=self.root)
            else:
                emp_id = self.var_name.get()
                cur.execute("select *from category where cid=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Error,Please try again", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Delete Category?", parent=self.root)
                    if op == True:
                        cur.execute("delete from category where cid=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Category Deleted Successfully", parent=self.root)
                        self.show()  # show the updated table
                        self.clear_input_field()
                        con.close()

        except Exception as ex:
            messagebox.showerror("Error",f"An error occured:{str(ex)}", parent=self.root)
            self.show()



    def clear_input_field(self):
        self.var_name.set('')

if __name__ == "__main__":
     root = Tk()
     obj = CategoryClass(root)
     root.mainloop()
