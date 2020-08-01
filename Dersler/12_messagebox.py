import tkinter as tk
from tkinter import messagebox


def button_click():
    # res = messagebox.askokcancel("askokcancel", "OK CANCEL")
    # res = messagebox.askquestion("askquestion", "QUESTION")
    # res = messagebox.askretrycancel("askretrycancel", "RETRY CANCEL")
    # res = messagebox.askyesno("askyesno", "YES NO")
    # res = messagebox.askyesnocancel("askyesnocancel", "YES NO CANCEL")
    # res = messagebox.showerror("showerror", "ERROR")
    # res = messagebox.showinfo("showinfo", "INFO")
    # res = messagebox.showwarning("showwarning", "WARNING")
    # print(res)
    pass


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("200x200")

b = tk.Button(root, text="Click", command=button_click)
b.place(anchor=tk.CENTER, relx=0.5, rely=0.5)

root.mainloop()
