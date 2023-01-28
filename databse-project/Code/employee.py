from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class employeeClass:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1100x500+80+120")
        self.root.config(bg="white")
        self.root.title("سیستم مدیریت انبارداری")
        self.root.focus_force()
        #============================
        # All variables
        self.var_search_by = StringVar()
        self.var_txt_search = StringVar()
        self.var_emp_id = StringVar()
        self.var_email = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()
        #=======searchFrame==========
        searchFrame = LabelFrame(self.root,text="جستجوی کارمندان", font=("goudy old style",20),bd=2, relief=RIDGE,bg="white")
        searchFrame.place(x=250, y=20, width=600,height=70)
        #=======option===============
        cmb_search = ttk.Combobox(searchFrame,textvariable=self.var_search_by, values=("انتخاب","نام","شماره تلفن","ایمیل"),state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_search.place(x=10, y=4, width=180)
        cmb_search.current(0)


        txt_search = Entry(searchFrame,font=("goudy old style", 15),textvariable=self.var_txt_search, bg="lightyellow").place(x=200, y=4)
        btn_search = Button(searchFrame,text="جستجو",command=self.search, font=(
            "goudy old style", 13), bg="#4caf50", fg="white", cursor="hand2").place(x=430, y=2, width=150, height=30)
        #=======title=================
        title = Label(self.root, text="اطلاعات کارمندان", font=("goudy old style", 15),bg="#0f4d7d",fg="white").place(x=0,y=100, width=1100)


        #=======content===============
        #=========row1================
        lbl_empid =         lbl_empid = Label(self.root, text="کد پرسنلی:",font=("goudy old style", 13), bg="white").place(x=50, y=150)
        lbl_gender = Label(self.root, text="جنسیت:",font=("goudy old style", 13), bg="white").place(x=350, y=150)
        lbl_contact = Label(self.root, text="تلفن:", font=("goudy old style", 13), bg="white").place(x=750, y=150)
        txt_empid = Entry(self.root,textvariable=self.var_emp_id, font=(
            "goudy old style", 13), bg="lightyellow").place(x=150, y=150, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=(
            "انتخاب", "مرد", " زن", "سایر"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_gender.current(0)
        cmb_gender.place(x=500, y=150, width=180)
        txt_contact = txt_empid = Entry(self.root, textvariable=self.var_contact, font=(
            "goudy old style", 13), bg="lightyellow").place(x=850, y=150, width=180)
        #==========row2==============
        lbl_name = lbl_name = Label(self.root, text=" نام:", font=(
            "goudy old style", 13), bg="white").place(x=50, y=190)
        lbl_dob = Label(self.root, text="تاریخ تولد:", font=(
            "goudy old style", 13), bg="white").place(x=350, y=190)
        lbl_doj = Label(self.root, text="تاریخ ورود:", font=(
            "goudy old style", 13), bg="white").place(x=750, y=190)
        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "goudy old style", 13), bg="lightyellow").place(x=150, y=190, width=180)
        tex_dob = Entry(self.root, textvariable=self.var_dob, font=(
            "goudy old style", 13), bg="lightyellow").place(x=500, y=190, width=180)
        txt_doj = txt_empid = Entry(self.root, textvariable=self.var_doj, font=(
            "goudy old style", 13), bg="lightyellow").place(x=850, y=190, width=180)
        # ==========row3==============
        lbl_email = Label(self.root, text="ایمل:", font=(
            "goudy old style", 13), bg="white").place(x=50, y=230)
        lbl_password = Label(self.root, text="رمز:", font=(
            "goudy old style", 13), bg="white").place(x=350, y=230)
        lbl_utype = Label(self.root, text="نوع کاربر:", font=(
            "goudy old style", 13), bg="white").place(x=750, y=230)
        txt_email = Entry(self.root, textvariable=self.var_email, font=(
            "goudy old style", 13), bg="lightyellow").place(x=150, y=230, width=180)
        tex_password = Entry(self.root, textvariable=self.var_pass, font=(
            "goudy old style", 13), bg="lightyellow").place(x=500, y=230, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=(
            "مدیر", "کارمند"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_utype.current(0)
        cmb_utype.place(x=850, y=230, width=180)
        # ==========row3==============
        lbl_address = Label(self.root, text="آدرس:", font=(
            "goudy old style", 13), bg="white").place(x=50, y=270)
        lbl_salary = Label(self.root, text="حقوق:", font=(
            "goudy old style", 13), bg="white").place(x=500, y=270)
        self.txt_address = Text(self.root, font=(
            "goudy old style", 13), bg="lightyellow")
        self.txt_address.place(x=150, y=270, width=300, height=60)
        tex_salary = Entry(self.root, textvariable=self.var_salary, font=(
            "goudy old style", 13), bg="lightyellow").place(x=600, y=270, width=180)
        #===========Buttons============
        btn_add = Button(self.root, text="اضافه کردن",command=self.add, font=(
            "goudy old style", 13), bg="#2196f3", fg="white", cursor="hand2").place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root, text="بروزرسانی",command=self.update, font=(
            "goudy old style", 13), bg="#4caf50", fg="white", cursor="hand2").place(x=620, y=305, width=110, height=28)
        btn_delete = Button(self.root, text="حذف",command=self.delete, font=(
            "goudy old style", 13), bg="#f44336", fg="white", cursor="hand2").place(x=740, y=305, width=110, height=28)
        btn_clear = Button(self.root, text="پاک کردن",command=self.clear, font=(
            "goudy old style", 13), bg="#607d8b", fg="white", cursor="hand2").place(x=860, y=305, width=110, height=28)
        #=========employee details======
        emp_frame = Frame(self.root,bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)
        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("eid","name", "email", "gender", "contact", "dob", "doj", "pass", "utype","address", "salary"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(fill=X, side=BOTTOM)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid", text="کد پرسنلی")
        self.EmployeeTable.heading("name", text="نام")
        self.EmployeeTable.heading("email", text="ایمیل")
        self.EmployeeTable.heading("gender", text="جنسیت")
        self.EmployeeTable.heading("contact", text="شماره تلفن")
        self.EmployeeTable.heading("dob", text="تاریخ تولد")
        self.EmployeeTable.heading("doj", text="تاریخ ورود")
        self.EmployeeTable.heading("pass", text="رمز")
        self.EmployeeTable.heading("utype", text="نوع کاربری")
        self.EmployeeTable.heading("address", text="آدرس")
        self.EmployeeTable.heading("salary", text="حقوق")
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
    #====================================================================
    def add(self):
        con = sqlite3.connect(database=r'wms.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("خطا","کد پرسنلی الزامی است",parent = self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Eroof", "این کد پرسنلی وجود دارد، کد دیگری را امتحان کنید",parent = self.root)
                else:
                    cur.execute(
                        "Insert into employee (eid,name, email, gender, contact, dob, doj, pass , utype,address, salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
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
                            self.var_salary.get(),
                        ))
                    con.commit()
                    self.show()
                    messagebox.showinfo("موفقیت آمیز","کاربر با موفقیت اضافه شد", parent=self.root)
        except Exception as ex:
            messagebox.showerror("خطا", f"خطای رخ داده : {str(ex)}", parent=self.root)
    

    def show(self):
        con = sqlite3.connect(database=r'wms.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("خطا", f"خطای رخ داده : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f))
        row = content['values']
        #print(row)
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
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])

    def update(self):
        con = sqlite3.connect(database=r'wms.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "خطا", "کد پرسنلی الزامی است", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",
                            (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Eroof", "کد پرسنلی وارد شده اشتباه میباشد", parent=self.root)
                else:
                    cur.execute(
                        "Update employee set name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, utype=?, address=?, salary=? where eid=?", (
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
                            self.var_emp_id.get(),
                        ))
                    con.commit()
                    self.show()
                    messagebox.showinfo("موفقیت آمیز", "کاربر با موفقیت بروزرسانی شد", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "خطا", f"خطای رخ داده : {str(ex)}", parent=self.root)



    def delete(self):
        con = sqlite3.connect(database=r'wms.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "خطا", "کد پرسنلی الزامی است", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",
                            (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Eroof", "کد پرسنلی وارد شده اشتباه میباشد", parent=self.root)
                else:
                    op = messagebox.askyesno("تاییدیه","آیا قصد پاکسازی کاربر را دارید؟",parent=self.root)
                    if op == True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("حذف", "کاربر با موفقیت حذف شد", parent=self.root)
                        self.clear()
                        self.show()
        except Exception as ex:
             messagebox.showerror(
                "خطا", f"خطای رخ داده : {str(ex)}", parent=self.root)
    


    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("انتخاب")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("مدیر")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
        self.var_txt_search.set("")
        self.var_search_by.set("انتخاب")


    def search(self):
        con = sqlite3.connect(database=r'wms.db')
        cur = con.cursor()
        try:
            if self.var_search_by.get() == "انتخاب":
                messagebox.showerror("خطا","آپشن جستجو باید انتخاب شود", parent=self.root)
            elif self.var_txt_search.get() == "":
                messagebox.showerror(
                    "خطا", "فیلد جستجو باید پر شود", parent=self.root)
            else:
                if self.var_search_by.get() == "نام":
                    cur.execute("select * from employee where name LIKE '%"+self.var_txt_search.get()+"%'")
                    rows = cur.fetchall()
                    if len(rows) !=0:
                        self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                        for row in rows:
                            self.EmployeeTable.insert('', END, values=row)
                    else:
                        messagebox.showerror(
                            "خطا", "کاربری یافت نشد", parent=self.root)
                elif self.var_search_by.get() == "ایمیل":
                    cur.execute("select * from employee where email LIKE '%"+self.var_txt_search.get()+"%'")
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        self.EmployeeTable.delete(
                            *self.EmployeeTable.get_children())
                        for row in rows:
                            self.EmployeeTable.insert('', END, values=row)
                    else:
                        messagebox.showerror(
                            "خطا", "کاربری یافت نشد", parent=self.root)
                elif self.var_search_by.get() == "شماره تلفن":
                    cur.execute("select * from employee where contact LIKE '%"+self.var_txt_search.get()+"%'")
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        self.EmployeeTable.delete(
                            *self.EmployeeTable.get_children())
                        for row in rows:
                            self.EmployeeTable.insert('', END, values=row)
                    else:
                        messagebox.showerror(
                            "خطا", "کاربری یافت نشد", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "خطا", f"خطای رخ داده : {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
