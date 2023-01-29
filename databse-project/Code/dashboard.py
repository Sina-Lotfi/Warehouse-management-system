from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
class WMS:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.title("سیستم مدیریت انبارداری")

        # ===========title==========
        self.icon_title = PhotoImage(
            file="images\logo1.png")
        title = Label(self.root, text="سیستم مدیریت انبارداری", font=("times", 40, "bold"), image=self.icon_title,
                      compound=RIGHT, bg="#010c48", fg="white", anchor="e", padx=20).place(x=0, y=0, relwidth=1, height=70)
        # ==========btn_logout======
        btn_logout = Button(self.root, text="خروج", font=(
            "times", 15, "bold"), bg="yellow", cursor="hand2").place(x=10, y=10, height=50, width=150)
        # ==========clock===========
        self.lbl_clock = Label(self.root, text="تاریخ: DD-MM-YYYY\t\t زمان: HH:MM:SS\t\t\t\t\t به سیستم مدیریت انبارداری خودش امدید ",
                                font=("times", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, height=30, relwidth=1)
        # ==========Righttmenu=========
        self.MenuLogo = Image.open(
            ".\images\menu_im.png")
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=1075, y=100, width=200, height=515)
        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)
        lbl_menu = Button(LeftMenu, text="منو", font=(
            "times", 20), bg="#009688").pack(side=TOP, fill=X)
        self.icon_side = PhotoImage(
            file="images\side.png")
        lbl_employee = Button(LeftMenu, text="کارمندان",command=self.employee,image=self.icon_side, compound=RIGHT,padx=20, anchor="e", font=(
            "times", 20, "bold"), bg="white", bd=2, cursor="hand2").pack(side=TOP, fill=X)
        lbl_supliers = Button(LeftMenu, text="تامین کنندگان",command=self.supplier, image=self.icon_side, compound=RIGHT, padx=20, anchor="e", font=(
            "times", 20, "bold"), bg="white", bd=2, cursor="hand2").pack(side=TOP, fill=X)
        lbl_category = Button(LeftMenu, text="دسته‌بندی",command=self.category, image=self.icon_side, compound=RIGHT, padx=20, anchor="e", font=(
            "times", 20, "bold"), bg="white", bd=2, cursor="hand2").pack(side=TOP, fill=X)
        lbl_product = Button(LeftMenu, text="محصولات",command=self.product, image=self.icon_side, compound=RIGHT, padx=20, anchor="e", font=(
            "times", 20, "bold"), bg="white", bd=2, cursor="hand2").pack(side=TOP, fill=X)
        lbl_sale = Button(LeftMenu, text="فروش",image=self.icon_side, compound=RIGHT,padx=20, anchor="e", font=(
            "times", 20, "bold"), bg="white", bd=2, cursor="hand2").pack(side=TOP, fill=X)
        lbl_exit = Button(LeftMenu, text="خروج", image=self.icon_side, compound=RIGHT, padx=20, anchor="e", font=(
            "times", 20, "bold"), bg="white", bd=2, cursor="hand2").pack(side=TOP, fill=X)
        #===========content=============
        self.lbl_employee = Label(self.root, text="تعداد کارمندان\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=(
            "goudy old style", 20, "bold"))
        self.lbl_employee.place(x=10, y=120, height=150, width=300)
        self.lbl_supliers = Label(self.root, text="تعداد منابع\n[ 0 ]", bd=5, relief=RIDGE, bg="#ff5722", fg="white", font=(
            "goudy old style", 20, "bold"))
        self.lbl_supliers.place(x=360, y=120, height=150, width=300)
        self.lbl_category = Label(self.root, text="تعداد دسته‌بندی\n[ 0 ]", bd=5, relief=RIDGE, bg="#009688", fg="white", font=(
            "goudy old style", 20, "bold"))
        self.lbl_category.place(x=710, y=120, height=150, width=300)
        self.lbl_products = Label(self.root, text="تعداد محصولات\n[ 0 ]", bd=5, relief=RIDGE, bg="#607d8b", fg="white", font=(
            "goudy old style", 20, "bold"))
        self.lbl_products.place(x=10, y=280, height=150, width=300)
        self.lbl_sales = Label(self.root, text="تعداد فروش\n[ 0 ]", bd=5, relief=RIDGE, bg="#ffc107", fg="white", font=(
            "goudy old style", 20, "bold"))
        self.lbl_sales.place(x=360, y=280, height=150, width=300)
        #===========Footer==============
        lbl_footer = Label(self.root, text="سیستم مدیریت انبارداری | توسعه داده شده توسط تیم هشتگ \n دانشگاه صنعتی همدان ترم پاییز ۴۰۱",font=("times", 10), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)
        #==============================================================================================
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)
        
    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)
if __name__ == "__main__":
    root = Tk()
    obj = WMS(root)
    root.mainloop()
