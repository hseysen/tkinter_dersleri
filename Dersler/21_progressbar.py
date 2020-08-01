import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("400x400")

# determinate / indeterminate

var = tk.IntVar()
pb = ttk.Progressbar(root, variable=var)
pb.pack()

b1 = ttk.Button(root, text="Get", takefocus=0, command=lambda: print(var.get()))
b1.pack()

b2 = ttk.Button(root, text="+5", takefocus=0, command=lambda: pb.step(5))
b2.pack()


# pb.config(maximum=20)

# pb.config(length=300)

# pb.config(orient=tk.VERTICAL)   # tk.HORIZONTAL

# pb.config(mode="indeterminate")

b3 = ttk.Button(root, text="Start", takefocus=0, command=lambda: pb.start(6))
b3.pack()

b4 = ttk.Button(root, text="Stop", takefocus=0, command=lambda: pb.stop())
b4.pack()


def helper():
    global var
    var.set(var.get() + 5)
    if pb['value'] >= pb['maximum']:
        return
    root.after(100, helper)


b5 = ttk.Button(root, text="Köməkçi Funksiya", takefocus=0, command=helper)
b5.pack()


root.mainloop()
