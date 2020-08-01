import tkinter as tk
import tkinter.ttk as ttk


def func():
    global x
    x += 1
    u.config(text=f"{x}")


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("500x500")

x = 0
u = ttk.Label(root, text=f"{x}")
u.pack()

b = ttk.Button(root, text="Click", command=lambda: func())
b.pack()

root.mainloop()


# pyinstaller --onefile -w --icon=cik.ico 30_py_to_exe.py

