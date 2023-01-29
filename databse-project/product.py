from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class productClass:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1100x500+80+120")
        self.root.config(bg="white")
        self.root.title("سیستم مدیریت انبارداری")
        self.root.focus_force()
        #==========================================================
        self.var_search_by = StringVar()
        self.var_txt_search = StringVar()
        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.cat_list = list()
        self.var_sup = StringVar()
        self.sup_list = list()
        self.fetch_cat_sup()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status= StringVar()
        product_Frame = Frame(self.root, bd=2, relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)
        # =======title=================
        title = Label(product_Frame, text="مدیریت محصولات", font=(
            "goudy old style", 18), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)
        #========== column 1 ======================
        lbl_category = Label(product_Frame, text="دسته‌بندی", font=(
            "goudy old style", 18), bg="white").place(x=30, y=60)
        lbl_supplier = Label(product_Frame, text="منبع", font=(
            "goudy old style", 18), bg="white").place(x=30, y=110)
        lbl_prooduct_name = Label(product_Frame, text="نام محصول", font=(
            "goudy old style", 18), bg="white").place(x=30, y=160)
        lbl_price = Label(product_Frame, text="قیمت ", font=(
            "goudy old style", 18), bg="white").place(x=30, y=210)
        lbl_qty = Label(product_Frame, text="مقدار", font=(
            "goudy old style", 18), bg="white").place(x=30, y=260)
        lbl_status = Label(product_Frame, text="وضعیت", font=(
            "goudy old style", 18), bg="white").place(x=30, y=310)

        # =======column2===============
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list, state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_cat.place(x=150, y=60, width=200)
        cmb_cat.current(0)
        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=self.sup_list, state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_sup.place(x=150, y=110, width=200)
        cmb_sup.current(0)
        txt_name = Entry(product_Frame,textvariable=self.var_name,font=("goudy old style", 15),bg="lightyellow").place(x=150, y=160, width=200)
        txt_price = Entry(product_Frame, textvariable=self.var_price, font=(
            "goudy old style", 15), bg="lightyellow").place(x=150, y=210, width=200)
        txt_qty = Entry(product_Frame, textvariable=self.var_qty, font=(
            "goudy old style", 15), bg="lightyellow").place(x=150, y=260, width=200)
        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=(
            "فعال","غیر فعال"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_status.place(x=150, y=310, width=200)
        cmb_status.current(0)
        # ===========Buttons============
        btn_add = Button(product_Frame, text="اضافه کردن", command=self.add, font=(
            "goudy old style", 13), bg="#2196f3", fg="white", cursor="hand2").place(x=10, y=400, width=100, height=40)
        btn_update = Button(product_Frame, text="بروزرسانی", command=self.update, font=(
            "goudy old style", 13), bg="#4caf50", fg="white", cursor="hand2").place(x=120, y=400, width=100, height=40)
        btn_delete = Button(product_Frame, text="حذف", command=self.delete, font=(
            "goudy old style", 13), bg="#f44336", fg="white", cursor="hand2").place(x=230, y=400, width=100, height=40)
        btn_clear = Button(product_Frame, text="پاک کردن", command=self.clear, font=(
            "goudy old style", 13), bg="#607d8b", fg="white", cursor="hand2").place(x=340, y=400, width=100, height=40)
        # =======searchFrame==========
        searchFrame = LabelFrame(self.root, text="جستجوی محصولات", font=(
            "goudy old style", 20), bd=2, relief=RIDGE, bg="white")
        searchFrame.place(x=480, y=10, width=600, height=80)
        # =======option===============
        cmb_search = ttk.Combobox(searchFrame, textvariable=self.var_search_by, values=(
            "انتخاب", "نام", "منبع", "دسته‌بندی"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_search.place(x=4, y=4, width=180)
        cmb_search.current(0)
        txt_search = Entry(searchFrame, font=("goudy old style", 15),
                           textvariable=self.var_txt_search, bg="lightyellow").place(x=200, y=4)
        btn_search = Button(searchFrame, text="جستجو", command=self.search, font=(
            "goudy old style", 13), bg="#4caf50", fg="white", cursor="hand2").place(x=430, y=2, width=150, height=30)
        # =========product details======
        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=480, y=100, width=600, height=390)
        scrolly = Scrollbar(p_frame, orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)
        self.Product_table = ttk.Treeview(p_frame, columns=("pid", "Category", "Supplier", "name", "price", "qty",
                                          "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(fill=X, side=BOTTOM)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Product_table.xview)
        scrolly.config(command=self.Product_table.yview)
        self.Product_table.heading("pid", text="کد محصول")
        self.Product_table.heading("Category", text="دسته‌بندی")
        self.Product_table.heading("Supplier", text="تامین کننده")
        self.Product_table.heading("name", text="نام")
        self.Product_table.heading("price", text="قیمت")
        self.Product_table.heading("qty", text="مقدار")
        self.Product_table.heading("status", text="وضعیت")
        self.Product_table["show"] = "headings"
        self.Product_table.column("pid", width=90)
        self.Product_table.column("Category", width=100)
        self.Product_table.column("Supplier", width=100)
        self.Product_table.column("name", width=100)
        self.Product_table.column("price", width=100)
        self.Product_table.column("qty", width=100)
        self.Product_table.column("status", width=100)
        self.Product_table.pack(fill=BOTH, expand=1)
        self.Product_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        # ====================================================================
    def fetch_cat_sup(self):
        self.cat_list.append("خالی")
        self.sup_list.append("خالی")
        con = sqlite3.connect(database=r'wms.db')
        cur = con.cursor()
        try:
            cur.execute("Select name from category")
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("انتخاب")
                for i in cat:
                    self.cat_list.append(i[0])
            
            cur.execute("Select name from supplier")
            sup = cur.fetchall()
            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("انتخاب")
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror(
            "خطا", f"خطای رخ داده : {str(ex)}", parent=self.root)


    def add(self):
        con = sqlite3.connect(database=r'wms.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == "انتخاب" or self.var_cat.get() == "خالی" or self.var_sup.get() == "انتخاب" or self.var_name.get() == "":
                messagebox.showerror(
                    "خطا", "تمامی فیلد ها الزامی هستند", parent=self.root)
            else:
                cur.execute("Select * from product where name=?",
                            (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "خطا", "این محصول وجود دارد، محصول دیگری را امتحان کنید", parent=self.root)
                else:
                    cur.execute(
                        "Insert into product (Category, Supplier, name, price, qty,status) values(?, ?, ?, ?, ?, ?)", (
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                        ))
                    con.commit()
                    self.show()
                    messagebox.showinfo(
                        "موفقیت آمیز", "محصول با موفقیت اضافه شد", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "خطا", f"خطای رخ داده : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'wms.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            rows = cur.fetchall()
            self.Product_table.delete(*self.Product_table.get_children())
            for row in rows:
                self.Product_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror(
                "خطا", f"خطای رخ داده : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.Product_table.focus()
        content = (self.Product_table.item(f))
        row = content['values']
        self.var_pid.set(row[0]),
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6]),
    def update(self):
        con = sqlite3.connect(database=r'wms.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror(
                    "خطا", "محصول را ازلیست انتخاب کنید", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",
                            (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Eroof", "محصول وارد شده اشتباه میباشد", parent=self.root)
                else:
                    cur.execute(
                        "Update product set Category=?, Supplier=?, name=?, price=?, qty=?, status=? where pid=?", (
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            self.var_pid.get(),
                        ))
                    con.commit()
                    self.show()
                    messagebox.showinfo(
                        "موفقیت آمیز", "محصول با موفقیت بروزرسانی شد", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "خطا", f"خطای رخ داده : {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'wms.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror(
                    "خطا", "محصول را از لیست انتخاب کنید", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",
                            (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Eroof", "محصول وارد شده اشتباه میباشد", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "تاییدیه", "آیا قصد حذف دارید؟", parent=self.root)
                    if op == True:
                        cur.execute("delete from product where pid=?",
                                    (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "حذف", "محصول با موفقیت حذف شد", parent=self.root)
                        self.clear()
                        self.show()
        except Exception as ex:
            messagebox.showerror(
                "خطا", f"خطای رخ داده : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_cat.set("انتخاب")
        self.var_sup.set("انتخاب")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("فعال")
        self.var_pid.set("")
        self.var_txt_search.set("")
        self.var_search_by.set("انتخاب")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'wms.db')
        cur = con.cursor()
        try:
            if self.var_search_by.get() == "انتخاب":
                messagebox.showerror(
                    "خطا", "آپشن جستجو باید انتخاب شود", parent=self.root)
            elif self.var_txt_search.get() == "":
                messagebox.showerror(
                    "خطا", "فیلد جستجو باید پر شود", parent=self.root)
            else:
                if self.var_search_by.get() == "نام":
                    cur.execute(
                        "select * from product where name LIKE '%"+self.var_txt_search.get()+"%'")
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        self.Product_table.delete(
                            *self.Product_table.get_children())
                        for row in rows:
                            self.Product_table.insert('', END, values=row)
                    else:
                        messagebox.showerror(
                            "خطا", "کاربری یافت نشد", parent=self.root)
                elif self.var_search_by.get() == "دسته‌بندی":
                    cur.execute(
                        "select * from product where Category LIKE '%"+self.var_txt_search.get()+"%'")
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        self.Product_table.delete(
                            *self.Product_table.get_children())
                        for row in rows:
                            self.Product_table.insert('', END, values=row)
                    else:
                        messagebox.showerror(
                            "خطا", "کاربری یافت نشد", parent=self.root)
                elif self.var_search_by.get() == "منبع":
                    cur.execute(
                        "select * from product where Supplier LIKE '%"+self.var_txt_search.get()+"%'")
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        self.Product_table.delete(
                            *self.Product_table.get_children())
                        for row in rows:
                            self.Product_table.insert('', END, values=row)
                    else:
                        messagebox.showerror(
                            "خطا", "کاربری یافت نشد", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "خطا", f"خطای رخ داده : {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
