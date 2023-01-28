from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class categoryClass:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1100x500+80+120")
        self.root.config(bg="white")
        self.root.title("سیستم مدیریت انبارداری")
        self.root.focus_force()


if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
