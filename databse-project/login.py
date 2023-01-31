from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("صفحه ورود")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        # ==== images==========
        self.phone_image = PhotoImage(file="images\phone.png")
        self.lbl_image_phone = Label(
            self.root, image=self.phone_image, bd=0).place(x=200, y=50)
        # =====login Frame============
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=650, y=90, width=350, height=460)

        title = Label(login_frame, text="فرم ورود", font=(
            "Elephant", 30, "bold"), bg="white").place(x=0, y=30, relwidth=1)

        lbl_user = Label(login_frame, text="کد پرسنلی", font=(
            "Elephant", 15), bg="white", fg="#767171").place(x=50, y=100)
        self.employee_id = StringVar()
        self.password = StringVar()
        tex_employee_id = Entry(login_frame, textvariable=self.employee_id, font=(
            "times", 15), bg="#ECECEC").place(x=50, y=140, width=250)

        lbl_pass = Label(login_frame, text="رمز ورود", font=(
            "Elephant", 15), bg="white", fg="#767171").place(x=50, y=190)
        tex_password = Entry(login_frame, textvariable=self.password, show="*", font=(
            "times", 15), bg="#ECECEC").place(x=50, y=240, width=250)

        btn_login = Button(login_frame, text="ورود", command=self.login, font=("Arial Rounded MT Bold", 15),
                           bg="#00B0F0", activebackground="#00B0F0", fg="white", activeforeground="white", cursor="hand2").place(x=50, y=300, width=250, height=35)
        hr = Label(login_frame, bg="lightgray").place(
            x=50, y=370, width=250, height=2)
        or_ = Label(login_frame, text="یا", fg="lightgray",
                    bg="white", font=("times", 15, "bold")).place(x=150, y=355)

        #btn_forget = Button(login_frame, text="slam",command=self.login, font=("times", 13), bg="white",
                            #fg="#00759E", bd=0, activebackground="white", activeforeground="#00759E").place(x=100, y=390)
        # ========= frame =============
        register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        register_frame.place(x=650, y=570, width=350, height=60)
        lbl_reg = Label(register_frame, text="سیستم مدیریت انبارداری سپهر", font=(
            "times", 13), bg="white").place(x=80, y=20)
        btn_forget = Button(login_frame, text="رمز خود  را فراموش کردید؟",command=self.forget, font=("times", 13), bg="white",
                            fg="#00759E", bd=0, activebackground="white", activeforeground="#00759E").place(x=100, y=390)
        # ======= animations images================
        self.im1 = ImageTk.PhotoImage(file="images/im1.png")
        self.im2 = ImageTk.PhotoImage(file="images/im2.png")
        self.im3 = ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image = Label(self.root, bg="white")
        self.lbl_change_image.place(x=367, y=153, width=240, height=428)

        self.animated()
        #======== All functions ===============
    def animated(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000, self.animated)

    def login(self):
        con = sqlite3.connect(database=r'wms.db')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password.get()=="":
                messagebox.showerror("خطا","تمامی فیلد هارا پر کنید",parent=self.root)
            else:
                cur.execute("Select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror(
                        "خطا", "نام کاربری یا رمز ورود اشتباه است دوباره امتحان کنید", parent=self.root)
                else:
                     self.root.destroy()
                     os.system("Python dashboard.py")
        except Exception as ex:
            messagebox.showerror(
                "خطا", f"خطای رخ داده : {str(ex)}", parent=self.root)

    def forget(self):
        con = sqlite3.connect(database=r'wms.db')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "":
                messagebox.showerror("خطا", "کد پرسنلی را وارد کنید",parent=self.root)
            else:
                cur.execute("Select email from employee where eid=?",
                            (self.employee_id.get(),))
                email = cur.fetchone()
                if email == None:
                    messagebox.showerror(
                        "خطا", "کد پرسنلی اشتباه است دوباره امتحان کنید", parent=self.root)
                else:
                    self.var_otp = StringVar()
                    self.var_new_pass = StringVar()
                    self.var_conf_pass = StringVar()
                    #===== forget window ==========
                    #call send_email() function
                    self.forget_win = Toplevel(self.root)
                    self.forget_win.title("بازیابی رمز ورود")
                    self.forget_win.geometry("400x350+500+100")
                    self.forget_win.focus_force()
                    title = Label(self.forget_win, text="بازیابی رمز ورود", font=("goudy old style", 15, "bold"), bg=("#3f51b5"), fg="white").pack(side=TOP, fill=X)
                    lbl_reset = Label(self.forget_win, text="ایمیل خود را برای بازیابی وارد کنید",font=("times", 15)).place(x=20,y=60)
                    tex_reset = Entry(self.forget_win, textvariable=self.var_otp, font=("times", 15),bg="lightyellow").place(x=20, y=100,width=250, height=30)
                    self.btn_reset = Button(self.forget_win, text="ثبت",font=("times", 15), bg="lightblue")
                    self.btn_reset.place(x=280,y=100,width=100, height=30)
                    lbl_new_pass = Label(self.forget_win, text="رمزعبور جدید را وارد نمایید", font=(
                        "times", 15)).place(x=20, y=160)
                    tex_new_pass = Entry(self.forget_win, textvariable=self.var_new_pass, font=(
                        "times", 15), bg="lightyellow").place(x=20, y=195, width=250, height=30)
                    lbl_c_pass = Label(self.forget_win, text="تایید رمزعبور", font=(
                        "times", 15)).place(x=20, y=225)
                    tex_c_pass = Entry(self.forget_win, textvariable=self.var_conf_pass, font=(
                        "times", 15), bg="lightyellow").place(x=20, y=255, width=250, height=30)
                    self.btn_update = Button(
                        self.forget_win, text="بروزرسانی", font=("times", 15), bg="lightblue")
                    self.btn_update.place(x=150, y=295, width=100, height=30)
        except Exception as ex:
            messagebox.showerror(
                "خطا", f"خطای رخ داده : {str(ex)}", parent=self.root)



root = Tk()
obj = Login_System(root)
root.mainloop()
