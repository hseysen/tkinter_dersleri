import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("700x700")


sp = ttk.Spinbox(root)
sp.pack()

b = ttk.Button(root, text="Get", takefocus=0, command=lambda: print(sp.get()))
b.pack()


# sp.config(from_=0, to=15)


qiteler = ("Afrika", "Amerika", "Antarktida", "Avropa", "Asiya", "Avstraliya")
sp.config(values=qiteler)


val = qiteler[0]


def update_value():
    global val
    val = sp.get()


sp.config(command=update_value)
sp.insert(0, qiteler[0])
b.config(command=lambda: print(val))


root.mainloop()

